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
	<div>
		<a href="/product/%s.html">
			<img src="/medias/images/%s" >
		</a>
	</div>
	<div>
		<strong>
			<a href="/product/%s.html" >
				%s
			</a>
		</strong>
	</div>
	<div>
		<em>
			<strong>
				price: $%s
			</strong>
		</em>
	</div>
	<div>
		<input type="text" value="1" class="qty" onblur="checkNum(this)" /> qty
		<input onclick="" type="button" value="ADD TO CART" class="add_cart" />
	</div>
</div>''' %(str(product.id), product.product_image, str(product.id), product.product_name, str(product.product_price))
	
	
	
