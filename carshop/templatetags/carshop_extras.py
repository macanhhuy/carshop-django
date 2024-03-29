# -*- coding:utf-8

from django.template import Library

register = Library()

@register.filter()
def get_range(value):
    """
     Filter - returns a list containing range made from given value
     Usage (in template):

     <ul>{% for i in 3|get_range %}
         <li>{{ i }}. Do something</li>
     {% endfor %}</ul>

     Results with the HTML:
     <ul>
         <li>0. Do something</li>
         <li>1. Do something</li>
         <li>2. Do something</li>
     </ul>

     Instead of 3 one may use the variable set in the views
    """
    return range(0, value)


@register.filter()
def product_generalor(product):
    ''' '''

    return '''
<div class="product1" id="pdiv%s">
	<ul>
		<li>
			<a href="/product/%s.html">
				<img src="/medias/images/%s" title="%s">
			</a>
		</li>
		<li style="height:40px;">
			<strong>
				<a href="/product/%s.html" title="%s">
					%s
				</a>
			</strong>
		</li>
		<li>
			<em>
				<strong style="color:red;font-size:14px;font-style:normal;">
					$%s
				</strong>
			</em>
		</li>
		<li>
			<input type="text" value="1" class="qty" id="qty%s" onblur="checkNum(this)"/> qty
		</li>
		<li>
			<input onclick="joinCart('%s')" type="button" value="ADD TO CART" class="add_cart"/>
		</li>
	</ul>

</div>
''' % (str(product.id), product.product_name.replace(' ', '-'), product.product_image, product.product_name,
       product.product_name.replace(' ', '-'), product.product_name,
       product.product_name, str(product.product_price), str(product.id), str(product.id), )


@register.filter()
def cart_item_generalor(cartItem):
    return '''
<div class="cartItem">
    <input type="hidden" value="%s"/>
    <input type="hidden" value="%s" style="margin-right:20px;"/>
    <img src="/medias/images/%s" style="height:80px;width:80px;margin-right:30px;">
    <strong style="margin-right:20px;width:200px;">%s</strong>
    <strong style="margin-right:20px;width:200px;">%s</strong>
    <input type="text" class="qty" value="%s" style="margin-right:20px;">
    <a href="/cart/remove/%s">remove</a>
</div>
    ''' % (cartItem.id, cartItem.product_id, cartItem.product.product_image, cartItem.product.product_name,
           cartItem.product.product_price, cartItem.quantity, cartItem.id,)


@register.filter()
def check_end_sprit(url):
    if url.endswith('/'):
        return url
    else:
        return url + '/'


@register.filter()
def space2line(name):
    return name.replace(' ', '_')


@register.filter()
def pager_generator(page):

    pager_html = '<div class="manu" style="margin-top:20px;margin-bottom:20px">'
    pager_html = pager_html + ('<a href="all-' + str(page.previous_page_number()) + '.html">< Prev</a>' if page.has_previous() else '')

    for page_num in page.paginator.page_range:
        if page_num == page.number:
            pager_html = pager_html + '<span class="current">' + str(page_num) + '</span>'
        else:
            pager_html = pager_html + '<a href="all-' + str(page_num) + '.html">' + str(page_num) + '</a>'

    pager_html = pager_html + ('<a href="all-' + str(page.next_page_number()) + '.html">Next ></a>' if page.has_next() else '')
    
    return pager_html