from django.urls import path
from django.http import HttpResponse
from django.shortcuts import redirect

def home_view(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>UptimeGuard - Website Monitoring Made Simple</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            .gradient-bg { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        </style>
    </head>
    <body class="bg-gray-50">
        <!-- Navigation -->
        <nav class="bg-white shadow-lg fixed w-full z-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between h-16">
                    <div class="flex items-center">
                        <div class="flex-shrink-0 flex items-center">
                            <div class="h-8 w-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                                <i class="fas fa-heartbeat text-white"></i>
                            </div>
                            <span class="ml-2 text-xl font-bold text-gray-900">UptimeGuard</span>
                        </div>
                    </div>
                    <div class="flex items-center space-x-4">
                        <a href="/login/" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition duration-200">
                            Sign In
                        </a>
                    </div>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="pt-20 pb-16 gradient-bg">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <div class="py-20">
                    <h1 class="text-5xl md:text-6xl font-bold text-white mb-6">
                        Monitor Your Websites
                        <span class="block text-yellow-300">24/7</span>
                    </h1>
                    <p class="text-xl text-blue-100 mb-8 max-w-3xl mx-auto">
                        Get instant alerts when your websites go down. Beautiful dashboards, 
                        real-time monitoring, and public status pages.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center">
                        <a href="/login/" class="bg-white text-blue-600 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 transition duration-200">
                            Start Monitoring Free
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section class="py-20 bg-white">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold text-gray-900 mb-4">Everything You Need</h2>
                    <p class="text-xl text-gray-600">Powerful monitoring tools for modern websites</p>
                </div>
                
                <div class="grid md:grid-cols-3 gap-8">
                    <div class="text-center p-8 rounded-xl bg-blue-50 hover:bg-blue-100 transition duration-200">
                        <div class="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i class="fas fa-clock text-white text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Real-time Monitoring</h3>
                        <p class="text-gray-600">Check your websites every 30 seconds with global monitoring locations</p>
                    </div>
                    
                    <div class="text-center p-8 rounded-xl bg-green-50 hover:bg-green-100 transition duration-200">
                        <div class="w-16 h-16 bg-green-500 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i class="fas fa-bell text-white text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Instant Alerts</h3>
                        <p class="text-gray-600">Get notified via email, SMS, or webhooks the moment something goes wrong</p>
                    </div>
                    
                    <div class="text-center p-8 rounded-xl bg-purple-50 hover:bg-purple-100 transition duration-200">
                        <div class="w-16 h-16 bg-purple-500 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i class="fas fa-chart-line text-white text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Beautiful Reports</h3>
                        <p class="text-gray-600">Detailed analytics and public status pages for your customers</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Pricing Section -->
        <section class="py-20 bg-gray-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold text-gray-900 mb-4">Simple Pricing</h2>
                    <p class="text-xl text-gray-600">Start free, upgrade as you grow</p>
                </div>
                
                <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
                    <div class="bg-white rounded-xl shadow-lg p-8 border-2 border-gray-200">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">Free</h3>
                        <p class="text-4xl font-bold text-gray-900 mb-4">$0<span class="text-lg text-gray-600">/month</span></p>
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>1 website</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>5-minute checks</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>Email alerts</li>
                        </ul>
                    </div>
                    
                    <div class="bg-white rounded-xl shadow-lg p-8 border-2 border-blue-500 relative">
                        <div class="absolute -top-4 left-1/2 transform -translate-x-1/2">
                            <span class="bg-blue-500 text-white px-4 py-1 rounded-full text-sm font-semibold">Popular</span>
                        </div>
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">Premium</h3>
                        <p class="text-4xl font-bold text-gray-900 mb-4">$9<span class="text-lg text-gray-600">/month</span></p>
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>5 websites</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>1-minute checks</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>SMS + Email alerts</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>Status pages</li>
                        </ul>
                    </div>
                    
                    <div class="bg-white rounded-xl shadow-lg p-8 border-2 border-gray-200">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">Pro</h3>
                        <p class="text-4xl font-bold text-gray-900 mb-4">$19<span class="text-lg text-gray-600">/month</span></p>
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>Unlimited websites</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>30-second checks</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>All integrations</li>
                            <li class="flex items-center"><i class="fas fa-check text-green-500 mr-3"></i>Priority support</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="bg-gray-900 text-white py-12">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <div class="flex items-center justify-center mb-4">
                    <div class="h-8 w-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center mr-2">
                        <i class="fas fa-heartbeat text-white"></i>
                    </div>
                    <span class="text-xl font-bold">UptimeGuard</span>
                </div>
                <p class="text-gray-400 mb-4">Professional website monitoring made simple</p>
                <div class="flex items-center justify-center space-x-4 text-sm text-gray-500">
                    <span>Contact: jvwcompany115@gmail.com</span>
                    <span>•</span>
                    <span><i class="fab fa-discord text-purple-400"></i> Discord server coming soon</span>
                </div>
            </div>
        </footer>
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
        <title>Sign In - UptimeGuard</title>
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
                               placeholder="Enter any username">
                    </div>
                    
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                        <input type="password" name="password" required 
                               class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" 
                               placeholder="Enter any password">
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
        <title>Dashboard - UptimeGuard</title>
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
                        <h1 class="text-xl font-semibold text-gray-900">UptimeGuard</h1>
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
                <div class="mb-8">
                    <h2 class="text-2xl font-bold text-gray-900 mb-2">Dashboard</h2>
                    <p class="text-gray-600">Monitor your websites and track performance</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center">
                            <div class="p-2 bg-green-100 rounded-lg">
                                <i class="fas fa-check-circle text-green-600 text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">All Online</p>
                                <p class="text-2xl font-semibold text-gray-900">0</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center">
                            <div class="p-2 bg-blue-100 rounded-lg">
                                <i class="fas fa-clock text-blue-600 text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Avg Response</p>
                                <p class="text-2xl font-semibold text-gray-900">--</p>
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
                                <p class="text-2xl font-semibold text-gray-900">--</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center">
                            <div class="p-2 bg-yellow-100 rounded-lg">
                                <i class="fas fa-globe text-yellow-600 text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Websites</p>
                                <p class="text-2xl font-semibold text-gray-900">0</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-lg shadow">
                    <div class="px-6 py-4 border-b border-gray-200">
                        <div class="flex justify-between items-center">
                            <h3 class="text-lg font-medium text-gray-900">Your Websites</h3>
                            <button class="bg-blue-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-blue-700 transition duration-200">
                                <i class="fas fa-plus mr-2"></i>Add Website
                            </button>
                        </div>
                    </div>
                    <div class="p-6">
                        <div class="text-center py-12">
                            <div class="mx-auto h-24 w-24 bg-gray-100 rounded-full flex items-center justify-center mb-4">
                                <i class="fas fa-globe text-gray-400 text-3xl"></i>
                            </div>
                            <h3 class="text-lg font-medium text-gray-900 mb-2">No websites yet</h3>
                            <p class="text-gray-600 mb-6">Add your first website to start monitoring</p>
                            <button class="bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition duration-200">
                                <i class="fas fa-plus mr-2"></i>Add Your First Website
                            </button>
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