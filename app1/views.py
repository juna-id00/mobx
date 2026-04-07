from django.shortcuts import render, redirect

from .models import mobile, laptop, tablet, smartwatch, headphones
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

# HOME
def home(request):
    return render(request, "layouts/home.html")


# PRODUCTS
def products(request):
    return render(
        request,
        "layouts/products.html",
        {
            "mobiles": mobile.objects.all(),
            "laptops": laptop.objects.all(),
            "tablets": tablet.objects.all(),
            "smartwatches": smartwatch.objects.all(),
            "headphones": headphones.objects.all(),
        }
    )


# PRODUCT VIEW
def product_view(request, type, id):

    Model = {
        "mobile": mobile,
        "laptop": laptop,
        "tablet": tablet,
        "smartwatch": smartwatch,
        "headphones": headphones,
    }.get(type)

    if Model is None:
        return redirect("products")

    try:
        product = Model.objects.get(id=id)
    except Model.DoesNotExist:
        return redirect("products")

    product.type = type  # IMPORTANT

    return render(request, "layouts/product_view.html", {"product": product})


# ------------------------------------------
# SIMPLE SESSION CART SYSTEM
# ------------------------------------------

def detect_product(id):
    """Find which model the product belongs to"""
    model_list = [mobile, laptop, tablet, smartwatch, headphones]

    for Model in model_list:
        try:
            product = Model.objects.get(id=id)
            return product, Model.__name__.lower()
        except Model.DoesNotExist:
            continue

    return None, None

@login_required(login_url="login")
def add_to_cart(request, type, id):
    cart = request.session.get("cart", [])

    Model = {
        "mobile": mobile,
        "laptop": laptop,
        "tablet": tablet,
        "smartwatch": smartwatch,
        "headphones": headphones,
    }.get(type)

    if Model is None:
        return redirect("products")

    try:
        Model.objects.get(id=id)
    except Model.DoesNotExist:
        return redirect("products")

    # Check if already exists
    for item in cart:
        if item["id"] == id and item["type"] == type:
            item["qty"] += 1
            request.session["cart"] = cart
            return redirect("cart")

    # Add new item
    cart.append({
        "id": id,
        "type": type,
        "qty": 1
    })

    request.session["cart"] = cart
    return redirect("cart")


def cart_page(request):
    cart = request.session.get("cart", [])
    items = []
    total_price = 0

    for c in cart:
        product, _ = detect_product(c["id"])
        items.append(
            {
                "product": product,
                "qty": c["qty"]
            }
        )
        total_price += product.price * c["qty"]

    return render(
        request,
        "items.html",
        {
            "items": items,
            "total_price": total_price
        }
    )


def increase_qty(request, id):
    cart = request.session.get("cart", [])

    for item in cart:
        if item["id"] == id:
            item["qty"] += 1

    request.session["cart"] = cart
    return redirect("cart")


def decrease_qty(request, id):
    cart = request.session.get("cart", [])

    for item in cart:
        if item["id"] == id and item["qty"] > 1:
            item["qty"] -= 1

    request.session["cart"] = cart
    return redirect("cart")


def remove_from_cart(request, id):
    cart = request.session.get("cart", [])
    cart = [i for i in cart if i["id"] != id]

    request.session["cart"] = cart
    return redirect("cart")





def cart_page(request):
    cart = request.session.get("cart", [])
    items = []
    total_price = 0

    for c in cart:
        product_id = c["id"]
        product_type = c["type"]

        Model = {
            "mobile": mobile,
            "laptop": laptop,
            "tablet": tablet,
            "smartwatch": smartwatch,
            "headphones": headphones,
        }.get(product_type)

        if Model:
            try:
                product = Model.objects.get(id=product_id)
                subtotal = product.price * c["qty"]
                total_price += subtotal

                items.append({
                    "product": product,
                    "qty": c["qty"]
                })

            except Model.DoesNotExist:
                pass

    return render(
        request,
        "layouts/cart.html",
        {
            "items": items,
            "total_price": total_price
        }
    )




def checkout(request):
    cart = request.session.get("cart", [])
    items = []
    total_price = 0

    for c in cart:
        product_id = c["id"]
        product_type = c["type"]

        Model = {
            "mobile": mobile,
            "laptop": laptop,
            "tablet": tablet,
            "smartwatch": smartwatch,
            "headphones": headphones,
        }.get(product_type)

        if Model:
            try:
                product = Model.objects.get(id=product_id)
                subtotal = product.price * c["qty"]

                items.append({
                    "product": product,
                    "qty": c["qty"],
                    "subtotal": subtotal
                })

                total_price += subtotal

            except Model.DoesNotExist:
                pass

    return render(
        request,
        "layouts/checkout.html",
        {
            "items": items,
            "total_price": total_price
        }
    )


from django.core.mail import send_mail
from django.conf import settings



def order_success(request):
    request.session["cart"] = []
    request.session.modified = True  # 🔥 IMPORTANT
    return render(request, "layouts/order_success.html")

def place_order(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")

        house = request.POST.get("house")
        place = request.POST.get("place")
        district = request.POST.get("district")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        landmark = request.POST.get("landmark")

        address = f"""{house}
{place}
{district}
{state} - {pincode}
Landmark: {landmark if landmark else 'N/A'}
"""

        cart = request.session.get("cart", [])
        message_lines = []
        total_price = 0

        for c in cart:

            product_id = c["id"]
            product_type = c["type"]

            Model = {
                "mobile": mobile,
                "laptop": laptop,
                "tablet": tablet,
                "smartwatch": smartwatch,
                "headphones": headphones,
            }.get(product_type)

            if Model:
                try:
                    product = Model.objects.get(id=product_id)

                    subtotal = product.price * c["qty"]
                    total_price += subtotal

                    message_lines.append(
                        f"{product.brand} {product.name} (x{c['qty']}) - ₹{subtotal}"
                    )

                except Model.DoesNotExist:
                    pass

        # ---------------- ADMIN EMAIL ---------------- #

        admin_message = f"""
New Order Received (MobX)

Customer Name: {name}
Phone: {phone}

Address:
{address}

Order Details:
--------------------
{chr(10).join(message_lines)}

Total Amount: ₹{total_price}
"""

        try:
            send_mail(
                subject="New Order - MobX",
                message=admin_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("✅ Admin email sent")

        except Exception as e:
            print("❌ Admin email failed:", e)

        # ---------------- CUSTOMER EMAIL ---------------- #

        user_email = request.user.email if request.user.is_authenticated else None

        if user_email:

            customer_message = f"""
Hello {name},

Thank you for your order with MobX! 🎉

📦 Order Summary:
--------------------
{chr(10).join(message_lines)}

💰 Total Amount: ₹{total_price}

🏠 Delivery Address:
{address}

We will process your order soon and keep you updated.

Happy shopping 🛒

MobX Team
"""

            try:
                send_mail(
                    subject="Your Order is Confirmed - MobX",
                    message=customer_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user_email],
                    fail_silently=False,
                )
                print("✅ Customer email sent")

            except Exception as e:
                print("❌ Customer email failed:", e)

        # ---------------- CLEAR CART ---------------- #

        request.session["cart"] = []
        request.session.modified = True

    return redirect("order_success")


import random
from django.shortcuts import render, redirect
from django.contrib import messages

def verify_otp(request):

    if request.method == "POST":

        user_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")
        email = request.session.get("email")

        if user_otp == session_otp:

            user = User.objects.get(email=email)

            user.is_active = True
            user.save()

            # SEND THANK YOU EMAIL
            send_mail(
                "Welcome to MobX 🎉",
                f"""
Hello {user.username},

Thank you for registering with MobX.

Your account has been successfully verified and is now active.

You can now explore our products and enjoy shopping with us.

Welcome aboard 🚀

MobX Team
""",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            # LOGIN USER
            login(request, user)

            # clean session
            request.session.pop("otp", None)
            request.session.pop("email", None)

            messages.success(request, "Account verified successfully!")

            return redirect("home")

        else:
            messages.error(request, "Invalid OTP")

    return render(request, "register/otp.html")

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")

        # CHECK IF USERNAME EXISTS
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        # CHECK IF EMAIL EXISTS
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_active = False
        user.save()

        otp = str(random.randint(100000, 999999))

        request.session["otp"] = otp
        request.session["email"] = email

        send_mail(
            "MobX OTP Verification",
            f"Your verification code is {otp}",
            settings.EMAIL_HOST_USER,
            [email],
        )

        return redirect("verify_otp")

    return render(request, "register/register.html")

from django.contrib.auth import authenticate, login


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # LOGIN EMAIL
            send_mail(
                "Login Alert - MobX",
                f"""
            Hello {user.username},

            We noticed a login to your MobX account.

            If this was you, no action is needed.
            If you did not log in, please change your 
            password immediately.

            MobX Security Team
            """,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return redirect("home")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "register/login.html")

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("home")