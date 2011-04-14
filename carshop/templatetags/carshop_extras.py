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
def product_general(product):
	'''
		
	'''
	
	return '''
<div class="product1">
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
			<input type="text" value="1" class="qty" onblur="checkNum(this)"/> qty
		</li>
		<li>
			<input onclick="" type="button" value="ADD TO CART" class="add_cart"/>
		</li>
	</ul>
</div>''' %(str(product.id), product.product_image, product.product_name, str(product.id), product.product_name, product.product_name, str(product.product_price))
	
	
	
