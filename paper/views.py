from django.shortcuts import render
from . models import Post
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,'base.html')

# used static backend
def home(request):
    News=[
        {
            'title':'কেশবপুরে জামায়াত প্রার্থীর বাড়িতে মধ্যরাতে ককটেল বিস্ফোরণ',
            'content':'যশোর-৬ আসনের (কেশবপুর) জামায়াত প্রার্থী মোক্তার আলীর বাড়িতে ককটেল বিস্ফোরণের ঘটনা ঘটেছে। গতকাল রোববার রাত একটার দিকে এ ঘটনা ঘটে।এ বিষয়ে আজ সোমবার জামায়াত প্রার্থীর প্রধান নির্বাচনী এজেন্ট সাইদুর রহমান সংবাদ সম্মেলন করেন। তিনি বলেন, এ ঘটনার পর ভোটার এবং সাধারণ মানুষের নিরাপত্তা নিয়ে আশঙ্কা তৈরি হয়েছে। সেই সঙ্গে জড়িত ব্যক্তিদের শাস্তি দাবি জানানো হয়েছে। তবে সুনির্দিষ্টভাবে কোনো দল বা কারও প্রতি তিনি অভিযোগ করেননি।',
            'image':'https://media.prothomalo.com/prothomalo-bangla%2F2026-01-13%2Fh0fre46c%2FWhatsApp_Image_2024_08_09_at_17_35_13.jpeg?rect=0%2C0%2C1200%2C800&w=622&auto=format%2Ccompress&fmt=avif',
        },
        {
            'title':'এভাবেই চ্যাম্পিয়নরা উঠে আসে—নেপালকে নিয়ে প্রশংসায় সাবেক ক্রিকেটাররা',
            'content':'এটি হতে পারত টি–টোয়েন্টি বিশ্বকাপের বড় অঘটনগুলোর একটি। বিশ্ব ক্রিকেটে লেখা হতো নেপাল ক্রিকেট দলের ইতিহাস গড়ার বীরোচিত এক গল্প। কিন্তু মাত্র ৪ রানের জন্য ইংল্যান্ডকে হারাতে পারল না নেপাল। খুব কাছে গিয়েও শেষ পর্যন্ত মন খারাপ করে মাঠ ছাড়তে হয়েছে এশিয়ান ক্রিকেটের উদীয়মান দলটির খেলোয়াড়দের।ইংল্যান্ডের দেওয়া ৭ উইকেটে ১৮৫ রানের লক্ষ্য তাড়া করতে গিয়ে নেপাল ৬ উইকেটে ১৮০ রানে তোলে।',
            'image':'https://media.prothomalo.com/prothomalo-bangla%2F2026-02-09%2Fom1y3lt2%2FCRICKET-ICC-MENS-T20-WC-2026-ENG-NEP-130235.jpg?w=622&auto=format%2Ccompress&fmt=avif',
        },
        {
            'title':'এভাবেই চ্যাম্পিয়নরা উঠে আসে—নেপালকে নিয়ে প্রশংসায় সাবেক ক্রিকেটাররা',
            'content':'এটি হতে পারত টি–টোয়েন্টি বিশ্বকাপের বড় অঘটনগুলোর একটি। বিশ্ব ক্রিকেটে লেখা হতো নেপাল ক্রিকেট দলের ইতিহাস গড়ার বীরোচিত এক গল্প। কিন্তু মাত্র ৪ রানের জন্য ইংল্যান্ডকে হারাতে পারল না নেপাল। খুব কাছে গিয়েও শেষ পর্যন্ত মন খারাপ করে মাঠ ছাড়তে হয়েছে এশিয়ান ক্রিকেটের উদীয়মান দলটির খেলোয়াড়দের।ইংল্যান্ডের দেওয়া ৭ উইকেটে ১৮৫ রানের লক্ষ্য তাড়া করতে গিয়ে নেপাল ৬ উইকেটে ১৮০ রানে তোলে।',
            'image':'https://media.prothomalo.com/prothomalo-bangla%2F2025-05-03%2Ftvdl6gx3%2FTrump-Tax.jpg?rect=0%2C0%2C621%2C414&w=622&auto=format%2Ccompress&fmt=avif'
        },
    ]
    Posts=Post.objects.all()   
    return render(request,'home.html',{
        'News':News,
        'Post':Posts
    })
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(name,email,message)
        messages.success(request,"Your message has been sent successfully ✅")

        

    return render(request,'contact.html')
