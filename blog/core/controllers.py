from flask import Blueprint,render_template,request,redirect,flash
from blog.core.models import create_blog,all_blogs,search_blog,blog_info,update_blog,delete_blog
core = Blueprint(__name__,'core')

@core.route('/')
def home():
    blogs=all_blogs()
    data = request.args.get('search_word')
    if data:
        blogs=search_blog(data)
    context = {
        'blogs': blogs
    }
    return render_template('core/home.html',**context)

@core.route('/create',methods=['GET','POST'])
def create():
    if request.method== 'POST':
        create_blog(**request.form,image='')
        flash('Blog was created')
        return redirect('/')
    return render_template('core/create.html')

@core.route('/blog/<int:blog_id>')
def blog_function(blog_id):
    blogs_info=blog_info(blog_id)
    context = {
        'blogs_info':blogs_info
    }
    return render_template('core/blog.html',**context)

@core.route('/update/<int:id>',methods=['GET','POST'])
def change_blog(id):
    blogs_info=blog_info(id)
    context = {
        'blogs_info':blogs_info
    }
    if request.method=='POST':
        update_blog(**request.form,id=id)
        flash('Blog updated')
        return redirect('/')
    return render_template('core/update.html',**context)

@core.route('/delete/<int:id>')
def remove_blog(id):
    delete_blog(id)
    flash('Blog deleted')
    return redirect('/')
