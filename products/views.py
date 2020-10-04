from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, ProductSubCategories, ProductCategories
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['best_selling'] = Product.objects.filter(best_selling=True)[:3]
        context['category_list'] = ProductCategories.objects.all()
        context['subcategory_list'] = ProductSubCategories.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['like_product'] = Product.objects.filter(category = self.object.category)[:3]
        context['product_image'] = Product.objects.filter(category = self.object.category)[:3]
        return context


def category_product_load(requeset):
    template_name = 'products/ajax/product_list.html'
    category = requeset.GET.get('category')
    products = Product.objects.filter(category=category)
    return render(requeset, template_name, {'products': products})


# This function is used to check if the parameter has value or not and return ture or false.
def is_valid_queryparam(param):
    return param != '' and param is not None


def product_filter_search_view(request):
    template_name = 'products/ajax/product_list.html'
    context = {}
    qs = Product.objects.all()
    category = request.GET.get('category')
    sub_category = request.GET.get('sub_category')
    search_text = request.GET.get('search_text')
    print(category)
    print(sub_category)
    if is_valid_queryparam(category):
        """
        This condition checks if the passed parameter is valid or not, using is_valid_queryparam function.
        """
        qs = qs.filter(category__name=category)
    if is_valid_queryparam(sub_category):
        """
        This condition checks if the passed parameter is valid or not, using is_valid_queryparam function.
        """
        qs = qs.filter(sub_category__name=sub_category)

    if is_valid_queryparam(search_text):
        """
        This condition checks if the passed parameter is valid or not, using is_valid_queryparam function.
        """
        qs = qs.filter(name__icontains=search_text)
    paginator = Paginator(qs, 15)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj

    return render(request, template_name, context)


