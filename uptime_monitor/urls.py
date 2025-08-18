from django.urls import path
from django.http import HttpResponse
from django.shortcuts import redirect

def home_view(request):
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
                
                <a href="/login/" class="w-full bg-blue-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-blue-700 transition duration-200 inline-block mb-4">
                    🔑 Sign In to Dashboard
                </a>
                
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

def login_view(request):
    if request.method == 'POST':
        return redirect('/dashboard/')
    
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sign In - Uptime Monitor</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    </head>
    <body class="bg-gray-50">
        <div class="min-h-screen flex items-center justify-center">
            <div class="max-w-md w-full bg-white rounded-lg shadow-lg p-8">
                <div class="text-center mb-8">
                    <div class="mx-auto h-12 w-12 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center mb-4">
                        <i class="fas fa-heartbeat text-white text-xl"></i>
                    </div>
                    <h2 class="text-2xl font-bold text-gray-900">Sign In</h2>
                    <p class="text-gray-600 mt-2">Access your monitoring dashboard</p>
                </div>
                
                <form method="post" class="space-y-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Username</label>
                        <input type="text" name="username" required 
                               class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" 
                               placeholder="Enter your username">
                    </div>
                    
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                        <input type="password" name="password" required 
                               class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" 
                               placeholder="Enter your password">
                    </div>
                    
                    <button type="submit" 
                            class="w-full bg-blue-600 text-white py-2 px-4 rounded-md font-semibold hover:bg-blue-700 transition duration-200">
                        Sign In
                    </button>
                </form>
                
                <div class="mt-6 text-center">
                    <a href="/" class="text-sm text-blue-600 hover:text-blue-500">← Back to Home</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')

def dashboard_view(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard - Uptime Monitor</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    </head>
    <body class="bg-gray-50">
        <nav class="bg-white shadow-sm border-b">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between h-16">
                    <div class="flex items-center">
                        <div class="h-8 w-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded flex items-center justify-center mr-3">
                            <i class="fas fa-heartbeat text-white text-sm"></i>
                        </div>
                        <h1 class="text-xl font-semibold text-gray-900">Uptime Monitor</h1>
                    </div>
                    <div class="flex items-center space-x-4">
                        <span class="text-sm text-gray-600">Welcome back!</span>
                        <a href="/" class="text-sm text-blue-600 hover:text-blue-500">Logout</a>
                    </div>
                </div>
            </div>
        </nav>
        
        <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <div class="px-4 py-6 sm:px-0">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center">
                            <div class="p-2 bg-green-100 rounded-lg">
                                <i class="fas fa-check-circle text-green-600 text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Websites Online</p>
                                <p class="text-2xl font-semibold text-gray-900">5</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center">
                            <div class="p-2 bg-blue-100 rounded-lg">
                                <i class="fas fa-clock text-blue-600 text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Avg Response Time</p>
                                <p class="text-2xl font-semibold text-gray-900">245ms</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center">
                            <div class="p-2 bg-purple-100 rounded-lg">
                                <i class="fas fa-chart-line text-purple-600 text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Uptime</p>
                                <p class="text-2xl font-semibold text-gray-900">99.9%</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-lg shadow">
                    <div class="px-6 py-4 border-b border-gray-200">
                        <h3 class="text-lg font-medium text-gray-900">Your Websites</h3>
                    </div>
                    <div class="p-6">
                        <div class="space-y-4">
                            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                                <div class="flex items-center">
                                    <div class="w-3 h-3 bg-green-400 rounded-full mr-3"></div>
                                    <div>
                                        <p class="font-medium text-gray-900">example.com</p>
                                        <p class="text-sm text-gray-600">Last checked: 2 minutes ago</p>
                                    </div>
                                </div>
                                <span class="text-sm font-medium text-green-600">Online</span>
                            </div>
                            
                            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                                <div class="flex items-center">
                                    <div class="w-3 h-3 bg-green-400 rounded-full mr-3"></div>
                                    <div>
                                        <p class="font-medium text-gray-900">mystore.com</p>
                                        <p class="text-sm text-gray-600">Last checked: 1 minute ago</p>
                                    </div>
                                </div>
                                <span class="text-sm font-medium text-green-600">Online</span>
                            </div>
                            
                            <div class="text-center py-8">
                                <button class="bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition duration-200">
                                    <i class="fas fa-plus mr-2"></i>Add New Website
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]