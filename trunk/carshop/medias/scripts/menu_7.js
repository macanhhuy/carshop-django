// (c) Copyright Microsoft Corporation.
// This source is subject to the Microsoft Permissive License.
// See http://www.microsoft.com/resources/sharedsource/licensingbasics/sharedsourcelicenses.mspx.
// All other rights reserved.

Type.registerNamespace('AjaxControlToolkit');

AjaxControlToolkit.HoverMenuBehavior = function(element) {
    /// <summary>
    /// The HoverMenuBehavior is used to display a popup whenever the target is hovered over
    /// </summary>
    /// <param name="element" type="Sys.UI.DomElement" domElement="true">
    /// DOM element the behavior is associated with
    /// </param>
    AjaxControlToolkit.HoverMenuBehavior.initializeBase(this, [element]);

    // Encapsulated behaviors
    this._hoverBehavior = null;
    this._popupBehavior = null;
    
    // Handler delegates
    this._mouseEnterHandler = null;
    this._mouseLeaveHandler = null;
    this._unhoverHandler = null;
    this._hoverHandler = null;
    
    // State variables
    this._inHover = null;
    this._oldClass = null;
    this._popupElement = null;
    
    // Property values
    this._popupElement = null;
    this._hoverCssClass = null;
    this._offsetX = 0;
    this._offsetY = 0;
    this._popDelay = 100;
    this._popupPosition = null;
}
AjaxControlToolkit.HoverMenuBehavior.prototype = {
    initialize : function() {
        /// <summary>
        /// Initialize the behavior
        /// </summary>
        AjaxControlToolkit.HoverMenuBehavior.callBaseMethod(this, 'initialize');

        // set up our delegates and handlers
        this._hoverHandler = Function.createDelegate(this, this._onHover);
        this._unhoverHandler = Function.createDelegate(this, this._onUnhover);
        this._mouseEnterHandler = Function.createDelegate(this, this._onmouseover);
        this._mouseLeaveHandler = Function.createDelegate(this, this._onmouseout);
        
        var e = this.get_element();
        $addHandler(e, "mouseover", this._mouseEnterHandler);
        $addHandler(e, "mouseout", this._mouseLeaveHandler);
        
        if (this._popupElement) {
            // setup the popup behavior
            this._popupBehavior = $create(AjaxControlToolkit.PopupBehavior, { "id":this.get_id()+"_PopupBehavior" }, null, null, this._popupElement);
            if (this._popupPosition) {
                this._popupBehavior.set_positioningMode(AjaxControlToolkit.HoverMenuPopupPosition.Absolute);
            } else {
                this._popupBehavior.set_positioningMode(AjaxControlToolkit.HoverMenuPopupPosition.Center);
            }
            
            // set up the hover behavior
            this._hoverBehavior = $create(AjaxControlToolkit.HoverBehavior, { "id":this.get_id()+"_HoverBehavior", "unhoverDelay":this._popDelay, "hoverElement":this._popupElement }, null, null, e);
            this._hoverBehavior.add_hover(this._hoverHandler);
            this._hoverBehavior.add_unhover(this._unhoverHandler);
        }
    },
    
    dispose : function() {
        /// <summary>
        /// Dispose the behavior
        /// </summary>

        // do cleanup
        if (this._popupBehavior) {
            this._popupBehavior.dispose();
            this._popupBehavior = null;
        }
        if (this._popupElement) {            
            this._popupElement = null;
        }
        if (this._mouseEnterHandler) {
            $removeHandler(this.get_element(), "mouseover", this._mouseEnterHandler);
        }
        if (this._mouseLeaveHandler) {            
            $removeHandler(this.get_element(), "mouseout", this._mouseLeaveHandler);
        }        
        if (this._hoverBehavior) {
            if (this._hoverHandler) {
                this._hoverBehavior.remove_hover(this._hoverHandler);
                this._hoverHandler = null;
            }
            if (this._unhoverHandler) {
                this._hoverBehavior.remove_hover(this._unhoverHandler);
                this._unhoverHandler = null;
            }
            this._hoverBehavior.dispose();
            this._hoverBehavior = null;
        }   
        AjaxControlToolkit.HoverMenuBehavior.callBaseMethod(this, 'dispose');       
    },
    
    _getLeftOffset : function() {
        /// <summary>
        /// Get the left offset of the popup
        /// </summary>
        /// <returns type="Number" integer="true">
        /// Left offset of the popup (in pixels)
        /// </returns>
 
        var defaultLeft = CommonToolkitScripts.getLocation(this.get_element()).x;
        var delta = 0;
        
        // this offset is always relative to the left edge of the hover element.
        switch(this._popupPosition) {
            case AjaxControlToolkit.HoverMenuPopupPosition.Left:
                // if it's positioned left, it's the width of the popup plus the offset
                delta = (-1 * this._popupElement.offsetWidth);
                break;
            case AjaxControlToolkit.HoverMenuPopupPosition.Right:
                // if it's to the right, it's the width of the hover element plus the offset.
                delta = this.get_element().offsetWidth;
                break; 
        }
        return delta + defaultLeft + this._offsetX;
    },
    
    _getTopOffset : function() {
        /// <summary>
        /// Get the top offset of the popup
        /// </summary>
        /// <returns type="Number" integer="true">
        /// Left offset of the popup (in pixels)
        /// </returns>

        var defaultTop = CommonToolkitScripts.getLocation(this.get_element()).y;
        var delta = 0;
    
        // this offset is always relative to the top edge of the hover element.
        switch(this._popupPosition) {
            case AjaxControlToolkit.HoverMenuPopupPosition.Top:
                // if it's Top positioned, it's the height of the popup plus the offset.
                delta = (-1 * this._popupElement.offsetHeight);
                break;
            case AjaxControlToolkit.HoverMenuPopupPosition.Bottom:
                // if it's bottom positioned it's the height of the hover element plus the offset
                delta = this.get_element().offsetHeight;
                break;
        }
        return defaultTop + delta + this._offsetY;      
    },
        
    _onHover : function() {
        /// <summary>
        /// Display the popup when the target is hovered over
        /// </summary>

        if (this._inHover) return;
        this._inHover = true;

        AjaxControlToolkit.HoverMenuBehavior.callBaseMethod(this, 'populate');
     
        this._popupBehavior.show();
        if (CommonToolkitScripts.getCurrentStyle(this._popupElement, 'display') == 'none') {
            this._popupElement.style.display = 'block';
        }
        this._popupBehavior.set_x(this._getLeftOffset());
        this._popupBehavior.set_y(this._getTopOffset());
    },
    
    _onUnhover : function() {
        /// <summary>
        /// Hide the popup when the target is no longer hovered
        /// </summary>
        this._inHover = false;
        this._resetCssClass(); 
        this._popupBehavior.hide();
    },
    
    _onmouseover : function() {
        /// <summary>
        /// Handler to change the CSS class when hovered over
        /// </summary>

        // set up the CSS class
        var e = this.get_element();
        if (this._hoverCssClass && e.className != this._hoverCssClass) {
            this._oldClass = e.className;
            e.className = this._hoverCssClass;
        }    
    },
    
    _onmouseout : function() {
        /// <summary>
        /// Handler to reset the CSS class when no longer hovering
        /// </summary>
        this._resetCssClass(); 
    },
 
    _resetCssClass : function() {
        /// <summary>
        /// Reset the CSS class if we changed it while hovering
        /// </summary>

        // make sure we're not still in hover mode, and that the class is
        // currently the hover class.
        var e = this.get_element();
        if (!this._inHover && this._hoverCssClass && e.className == this._hoverCssClass) {
            e.className = this._oldClass;
        }
    },
    
    get_popupElement : function() {
        /// <value type="Sys.UI.DomElement" domElement="true">
        /// Popup that is displayed when hovering
        /// </value>
        return this._popupElement;
    },
    set_popupElement : function(value) {
        if (this._popupElement != value) {
            this._popupElement = value;
            if (this.get_isInitialized() && this._hoverBehavior) {
                this._hoverBehavior.set_hoverElement(this._popupElement);
            }
            this.raisePropertyChanged('popupElement');
        }
    },
    
    get_HoverCssClass : function() {
        /// <value type="String">
        /// CSS class used when hovering
        /// </value>
        return this._hoverCssClass;
    },
    set_HoverCssClass : function(value) {
        if (this._hoverCssClass != value) {
            this._hoverCssClass = value;
            this.raisePropertyChanged('HoverCssClass');
        }
    },
    
    get_OffsetX : function() {
        /// <value type="Number" integer="true">
        /// The number of pixels to offset the popup from it's default position horizontally
        /// </value>
        return this._offsetX;
    },
    set_OffsetX : function(value) {
        if (this._offsetX != value) {
            this._offsetX = value;
            this.raisePropertyChanged('OffsetX');
        }
    },
    
    get_OffsetY : function() {
        /// <value type="Number" integer="true">
        /// The number of pixels to offset the popup from it's default position vertically
        /// </value>
        return this._offsetY;
    },
    set_OffsetY : function(value) {
        if (this._offsetY != value) {
            this._offsetY = value;
            this.raisePropertyChanged('OffsetY');
        }
    },
    
    get_PopupPosition : function() {
        /// <value type="AjaxControlToolkit.HoverMenuPopupPosition">
        /// Where the popup should be positioned relative to the target control.
        /// Can be Left (Default), Right, Top, Bottom, Center.
        /// </value>
        return this._popupPosition;
    },
    set_PopupPosition : function(value) {
        if (this._popupPosition != value) {
            this._popupPosition = value;
            this.raisePropertyChanged('PopupPosition');
        }
    },
    
    get_PopDelay : function() {
        /// <value type="Number">
        /// The time delay from when the mouse enters the target to when the popup is shown, in milliseconds. Default is 100.
        /// </value>
        return this._popDelay;
    },
    set_PopDelay : function(value) {
        if (this._popDelay != value) {
            this._popDelay = value;
            this.raisePropertyChanged('PopDelay');
        }
    }
}
AjaxControlToolkit.HoverMenuBehavior.registerClass('AjaxControlToolkit.HoverMenuBehavior', AjaxControlToolkit.DynamicPopulateBehaviorBase);
//    getDescriptor : function() {
//        var td = AjaxControlToolkit.HoverMenuBehavior.callBaseMethod(this, 'getDescriptor');
//        td.addProperty('PopupControlID', String);        
//        td.addProperty('HoverCssClass', String);        
//        td.addProperty('OffsetX', Number);        
//        td.addProperty('OffsetY', Number);                
//        td.addProperty('PopDelay', Number);                
//        td.addProperty('PopupPosition', String);        
//        return td;
//    },


AjaxControlToolkit.HoverMenuPopupPosition = function() {
    /// <summary>
    /// Where the popup should be positioned relative to the target control
    /// </summary>
    /// <field name="Center" type="Number" integer="true" />
    /// <field name="Top" type="Number" integer="true" />
    /// <field name="Left" type="Number" integer="true" />
    /// <field name="Bottom" type="Number" integer="true" />
    /// <field name="Right" type="Number" integer="true" />
    throw Error.invalidOperation();
}
AjaxControlToolkit.HoverMenuPopupPosition.prototype = {
    Center: 0,
    Top: 1,
    Left: 2,
    Bottom: 3,
    Right: 4
}
AjaxControlToolkit.HoverMenuPopupPosition.registerEnum('AjaxControlToolkit.HoverMenuPopupPosition');
if(typeof(Sys)!=='undefined')Sys.Application.notifyScriptLoaded();