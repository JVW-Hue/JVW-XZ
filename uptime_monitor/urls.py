from django.urls import path
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Website Uptime Monitor SaaS</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    </head>
    <body class="bg-gray-50">
        <div class="min-h-screen flex items-center justify-center">
            <div class="max-w-md w-full bg-white rounded-lg shadow-lg p-8 text-center">
                <div class="mx-auto h-16 w-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center mb-6">
                    <i class="fas fa-heartbeat text-white text-2xl"></i>
                </div>
                <h1 class="text-3xl font-bold text-gray-900 mb-4">Website Uptime Monitor</h1>
                <p class="text-gray-600 mb-6">Professional SaaS for monitoring website uptime and performance</p>
                <div class="space-y-4">
                    <div class="bg-blue-50 p-4 rounded-lg">
                        <h3 class="font-semibold text-blue-900">✅ Features</h3>
                        <ul class="text-sm text-blue-700 mt-2 space-y-1">
                            <li>• Real-time monitoring</li>
                            <li>• Email & SMS alerts</li>
                            <li>• Beautiful dashboards</li>
                            <li>• Public status pages</li>
                        </ul>
                    </div>
                    <div class="bg-green-50 p-4 rounded-lg">
                        <h3 class="font-semibold text-green-900">💰 Pricing</h3>
                        <ul class="text-sm text-green-700 mt-2 space-y-1">
                            <li>• Free: 1 website</li>
                            <li>• Premium: $9/mo - 5 websites</li>
                            <li>• Pro: $19/mo - Unlimited</li>
                        </ul>
                    </div>
                    <div class="bg-purple-50 p-4 rounded-lg">
                        <h3 class="font-semibold text-purple-900">🚀 Ready to Launch</h3>
                        <p class="text-sm text-purple-700 mt-2">Production-ready SaaS application</p>
                        <p class="text-xs text-purple-600 mt-1">Contact: jvwcompany115@gmail.com</p>
                        <p class="text-xs text-purple-600">Discord server coming soon!</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')

urlpatterns = [
    path('', simple_view, name='home'),
]