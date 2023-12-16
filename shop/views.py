

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Product, Category


from django.db.models import Q
from .forms import AddProductForm,EditProductForm
from django.urls import reverse_lazy


# Create your views here.




class ProductListView(ListView):
    model = Product
   

    template_name = 'shop/home.html'
    context_object_name = 'products'
    

# class LaptopListView(ListView):
#     model =  Category
#     template_name = 'shop/home.html'
#     context_object_name = 'categories'

@method_decorator(login_required,name='dispatch')
@method_decorator(staff_member_required,name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = AddProductForm
    success_url = reverse_lazy('shop:home')
    template_name = 'shop/add_products.html'

@method_decorator(login_required,name='dispatch')
@method_decorator(staff_member_required,name='dispatch')
class ProductEditView(UpdateView):
    model = Product
    form_class = AddProductForm
    success_url = reverse_lazy('shop:home')
    template_name = 'shop/add_products.html'
    

@method_decorator(login_required,name='dispatch')
@method_decorator(staff_member_required,name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop:home')


        
    
   



class CateoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'category'


def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'shop/category_product_list.html',{'data':data})
