from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect

def home_view(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>UptimeGuard - Website Monitoring</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    </head>
    <body class="bg-gray-50">
        <div class="min-h-screen flex items-center justify-center">
            <div class="max-w-md w-full bg-white rounded-lg shadow-lg p-8 text-center">
                <div class="mx-auto h-16 w-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center mb-6">
                    <i class="fas fa-heartbeat text-white text-2xl"></i>
                </div>
                <h1 class="text-3xl font-bold text-gray-900 mb-4">UptimeGuard</h1>
                <p class="text-gray-600 mb-6">Professional Website Monitoring SaaS</p>
                
                <div class="space-y-3">
                    <a href="/auth/signup/" class="w-full bg-blue-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-blue-700 transition duration-200 inline-block">
                        📝 Sign Up Free
                    </a>
                    <a href="/auth/login/" class="w-full bg-gray-100 text-gray-700 py-3 px-4 rounded-lg font-semibold hover:bg-gray-200 transition duration-200 inline-block">
                        🔐 Sign In
                    </a>
                    <a href="/billing/pricing/" class="w-full bg-green-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-green-700 transition duration-200 inline-block">
                        💰 View Pricing
                    </a>
                    <a href="/dashboard/" class="w-full bg-purple-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-purple-700 transition duration-200 inline-block">
                        📊 Dashboard
                    </a>
                </div>
                
                <div class="mt-8 text-sm text-gray-500">
                    <p>✓ Real-time monitoring</p>
                    <p>✓ PayPal payments</p>
                    <p>✓ Beautiful dashboards</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('auth/', include('core.urls')),
    path('dashboard/', include('monitoring.urls')),
    path('billing/', include('billing.urls')),
    path('workflows/', lambda request: redirect('/')),
]