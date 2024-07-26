from django.shortcuts import render
from .import models

# Create your views here.
def home(request):
    # blogs=[
    #     {"id":1,"Subject":"Baudhayana Sulba Sutra",'Author':"Baudhayana","About the Book":"Believed to have been written around the 8th century BCE, this is one of the oldest mathematical texts. It laid the foundations of Indian mathematics and was influential in South Asia. "},
    #     {"id":2,"Subject":" Elements of Algebra","Author":"Leonhard Euler","About the Book":"Euler's textbook on elementary algebra is one of the first to set out algebra in the modern form we would recognize today."},
    #     {"id":3,"Subject":"Reflections on the algebraic solutions of equations","Author":"Joseph Louis Lagrange ","About the Book":" Made the prescient observation that the roots of the Lagrange resolvent of a polynomial equation are tied to permutations of the roots of the original equation,"}

    # ]
    blogs=models.post.objects.all()
    return render(request,"Blog/home.html",{"blog":blogs})
def blog_details(request,idd):
    # blogs={
    #     1:{"Subject":"Baudhayana Sulba Sutra",'Author':"Baudhayana","Details":"Believed to have been written around the 8th century BCE, this is one of the oldest mathematical texts. It laid the foundations of Indian mathematics and was influential in South Asia. "},
    #     2:{"Subject":" Elements of Algebra","Author":"Leonhard Euler","Details":"Euler's textbook on elementary algebra is one of the first to set out algebra in the modern form we would recognize today."},
    #     3:{"Subject":"Reflections on the algebraic solutions of equations","Author":"Joseph Louis Lagrange ","Details":" Made the prescient observation that the roots of the Lagrange resolvent of a polynomial equation are tied to permutations of the roots of the original equation,"}
    # }
    
    # detailed_blog=blogs.get(idd)
    detailed_blog=models.post.objects.all()
       
    
    return render(request,"Blog/blog_details.html",{"blog":detailed_blog[idd-1]})    
     


