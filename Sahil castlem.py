<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sahil Castle - Entry Gate</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
            user-select: none;
            -webkit-tap-highlight-color: transparent;
            margin: 0;
            padding: 0;
        }
        
        .dark {
            background: linear-gradient(135deg, #000000, #111827, #1f2937);
        }
        
        .castle-tap {
            transition: transform 0.1s ease;
            cursor: pointer;
        }
        
        .castle-tap:active {
            transform: scale(0.95);
        }
        
        .coin-float {
            animation: coinFloat 1s ease-out forwards;
            pointer-events: none;
            z-index: 10;
        }
        
        @keyframes coinFloat {
            0% { opacity: 1; transform: translateY(0); }
            100% { opacity: 0; transform: translateY(-60px); }
        }
        
        .energy-bar {
            background: linear-gradient(90deg, #3b82f6, #1d4ed8);
            transition: width 0.3s ease;
        }
        
        .upgrade-card {
            background: linear-gradient(135deg, #1f2937, #374151);
            border: 1px solid #4b5563;
            transition: all 0.3s ease;
        }
        
        .dark .upgrade-card {
            background: linear-gradient(135deg, #111827, #1f2937);
        }
        
        .upgrade-card:hover {
            border-color: #3b82f6;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(59, 130, 246, 0.2);
        }
        
        .tab-button {
            transition: all 0.3s ease;
        }
        
        .tab-button.active {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: #fff;
        }
        
        .pulse-animation {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .gradient-text {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .sa-coin {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 30px;
            height: 30px;
            background-image: url('https://pfst.cf2.poecdn.net/base/image/2665579a543d3ca3e405b978c6575e4f51b0750520ad10ccd6bc707289130bfb?w=900&h=1500');
            background-size: cover;
            background-position: center;
            border-radius: 50%;
            font-weight: 800;
            font-size: 10px;
            color: #fff;
            text-shadow: 0 1px 2px rgba(0,0,0,0.8);
            border: 2px solid #fbbf24;
            box-shadow: 0 0 10px rgba(251, 191, 36, 0.5);
        }
        
        .sa-coin-large {
            width: 40px;
            height: 40px;
            font-size: 12px;
            border: 3px solid #fbbf24;
        }
        
        .castle-glow {
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.3);
        }
        
        .social-card {
            background: linear-gradient(135deg, #1e293b, #334155);
            border: 1px solid #475569;
            transition: all 0.3s ease;
        }
        
        .dark .social-card {
            background: linear-gradient(135deg, #111827, #1f2937);
        }
        
        .social-card:hover {
            border-color: #3b82f6;
            transform: translateY(-2px);
        }
        
        .reward-claimed {
            background: linear-gradient(135deg, #059669, #047857) !important;
        }

        .castle-coin-frame {
            position: relative;
            background-image: url('https://pfst.cf2.poecdn.net/base/image/2665579a543d3ca3e405b978c6575e4f51b0750520ad10ccd6bc707289130bfb?w=900&h=1500');
            background-size: cover;
            background-position: center;
            border: 3px solid #fbbf24;
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(251, 191, 36, 0.6), inset 0 0 10px rgba(0,0,0,0.3);
        }

        .castle-coin-frame::before {
            content: '';
            position: absolute;
            inset: -3px;
            border-radius: 50%;
            background: linear-gradient(45deg, #fbbf24, #f59e0b, #d97706, #fbbf24);
            z-index: -1;
        }
        
        /* Mobile optimizations */
        @media (max-width: 768px) {
            .castle-tap {
                width: 200px !important;
                height: 200px !important;
            }
            
            .text-8xl {
                font-size: 4rem !important;
            }
        }
        
        /* Input font size fix for mobile */
        input, select {
            font-size: 16px !important;
        }
        
        /* Loading state */
        .loading {
            opacity: 0.6;
            pointer-events: none;
        }

        /* Entry page styles */
        .entry-page {
            min-height: 100vh;
            background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
        }

        .social-task-card {
            background: linear-gradient(135deg, #1f2937, #374151);
            border: 2px solid #4b5563;
            transition: all 0.3s ease;
        }

        .social-task-card.completed {
            border-color: #10b981;
            background: linear-gradient(135deg, #064e3b, #065f46);
        }

        .social-task-card.pending {
            border-color: #f59e0b;
        }

        .access-code-input {
            background: linear-gradient(135deg, #1f2937, #374151);
            border: 2px solid #4b5563;
            color: #fff;
            letter-spacing: 0.2em;
            text-align: center;
            font-weight: bold;
            font-size: 1.2rem;
        }

        .access-code-input:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        }

        .floating-castle {
            animation: floatCastle 3s ease-in-out infinite;
        }

        @keyframes floatCastle {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        .glow-border {
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
        }

        .store-item {
            background: linear-gradient(135deg, #1f2937, #374151);
            border: 2px solid #4b5563;
            transition: all 0.3s ease;
        }

        .store-item:hover {
            border-color: #10b981;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.2);
        }

        .store-item.purchased {
            border-color: #10b981;
            background: linear-gradient(135deg, #064e3b, #065f46);
        }

        .dollar-coin {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, #10b981, #047857);
            border-radius: 50%;
            font-weight: 800;
            font-size: 10px;
            color: #fff;
            text-shadow: 0 1px 2px rgba(0,0,0,0.8);
            border: 2px solid #10b981;
            box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
        }

        .admin-panel {
            background: linear-gradient(135deg, #7c2d12, #991b1b);
            border: 2px solid #dc2626;
        }

        .game-saving {
            animation: savePulse 1s ease-in-out;
        }

        @keyframes savePulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
    </style>
</head>
<body class="bg-slate-900 dark:bg-gray-900 text-white">
    <!-- Entry Page -->
    <div id="entryPage" class="entry-page flex flex-col items-center justify-center p-6">
        <!-- Header -->
        <div class="text-center mb-8">
            <div class="floating-castle w-32 h-32 mx-auto mb-6 bg-gradient-to-br from-blue-500 to-blue-700 rounded-3xl flex items-center justify-center shadow-2xl castle-glow">
                <i class="fas fa-chess-rook text-6xl text-white"></i>
            </div>
            <h1 class="text-4xl font-bold gradient-text mb-2">Welcome to Sahil Castle</h1>
            <p class="text-slate-400 dark:text-gray-400">Enter the realm of castle building</p>
        </div>

        <!-- Access Requirements -->
        <div class="w-full max-w-md bg-slate-800 dark:bg-gray-800 rounded-lg p-6 mb-6">
            <h2 class="text-xl font-bold mb-4 text-center">🔐 Access Requirements</h2>
            <p class="text-sm text-slate-400 dark:text-gray-400 text-center mb-6">
                To protect our kingdom, you must prove your loyalty by following all our royal channels.
            </p>

            <!-- Social Media Tasks -->
            <div class="space-y-3 mb-6" id="socialTasks">
                <div class="social-task-card rounded-lg p-3 pending" data-task="facebook">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <i class="fab fa-facebook text-blue-500 text-xl"></i>
                            <div>
                                <div class="font-semibold text-sm">Follow on Facebook</div>
                                <div class="text-xs text-slate-400">Royal updates & news</div>
                            </div>
                        </div>
                        <button class="follow-btn bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-xs font-semibold" data-url="https://www.facebook.com/share/14FfTqnkdKu/">
                            Follow
                        </button>
                    </div>
                </div>

                <div class="social-task-card rounded-lg p-3 pending" data-task="tiktok">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <i class="fab fa-tiktok text-pink-500 text-xl"></i>
                            <div>
                                <div class="font-semibold text-sm">Follow on TikTok</div>
                                <div class="text-xs text-slate-400">Fun castle content</div>
                            </div>
                        </div>
                        <button class="follow-btn bg-pink-500 hover:bg-pink-600 text-white px-3 py-1 rounded text-xs font-semibold" data-url="https://www.tiktok.com/@sahilasadi967?_r=1&_d=ed009bm57edcj2&sec_uid=MS4wLjABAAAAyYcyUtYYdKyA98cGcUU04NmOkw22wmULV6FIz8P01R6VfJqkyjZj04afcwiXRzPb&share_author_id=7341417295719433221&sharer_language=en&source=h5_m&u_code=ed00a164kiddl8&timestamp=1753538240&user_id=7341417295719433221&sec_user_id=MS4wLjABAAAAyYcyUtYYdKyA98cGcUU04NmOkw22wmULV6FIz8P01R6VfJqkyjZj04afcwiXRzPb&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_iid=7466942113089160977&share_link_id=5ba85bc1-4f86-401a-b7b0-150d3af1eec9&share_app_id=1233&ugbiz_name=ACCOUNT&ug_btm=b8727%2Cb0229&social_share_type=5&enable_checksum=1">
                            Follow
                        </button>
                    </div>
                </div>

                <div class="social-task-card rounded-lg p-3 pending" data-task="youtube">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <i class="fab fa-youtube text-red-500 text-xl"></i>
                            <div>
                                <div class="font-semibold text-sm">Subscribe YouTube</div>
                                <div class="text-xs text-slate-400">Gaming tutorials</div>
                            </div>
                        </div>
                        <button class="follow-btn bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-xs font-semibold" data-url="https://www.youtube.com/@SahilAsadi-v7g">
                            Subscribe
                        </button>
                    </div>
                </div>

                <div class="social-task-card rounded-lg p-3 pending" data-task="whatsapp">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <i class="fab fa-whatsapp text-green-500 text-xl"></i>
                            <div>
                                <div class="font-semibold text-sm">Join WhatsApp</div>
                                <div class="text-xs text-slate-400">Community group</div>
                            </div>
                        </div>
                        <button class="follow-btn bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded text-xs font-semibold" data-url="https://chat.whatsapp.com/Hoh0Gx4DgLvH01f2mnrf6F?mode=ac_t">
                            Join
                        </button>
                    </div>
                </div>

                <div class="social-task-card rounded-lg p-3 pending" data-task="telegram">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <i class="fab fa-telegram text-blue-400 text-xl"></i>
                            <div>
                                <div class="font-semibold text-sm">Join Telegram</div>
                                <div class="text-xs text-slate-400">Royal announcements</div>
                            </div>
                        </div>
                        <button class="follow-btn bg-blue-400 hover:bg-blue-500 text-white px-3 py-1 rounded text-xs font-semibold" data-url="https://t.me/sahilcastlegam">
                            Join
                        </button>
                    </div>
                </div>
            </div>

            <!-- Completion Status -->
            <div class="text-center mb-4">
                <div class="text-sm text-slate-400">Progress: <span id="completionCount">0</span>/5 completed</div>
                <div class="w-full bg-slate-700 rounded-full h-2 mt-2">
                    <div class="bg-blue-500 h-2 rounded-full transition-all duration-300" id="progressBar" style="width: 0%"></div>
                </div>
            </div>

            <!-- Access Code Section -->
            <div id="codeSection" class="hidden">
                <div class="bg-green-900 border border-green-500 rounded-lg p-4 mb-4">
                    <div class="text-center">
                        <i class="fas fa-check-circle text-green-400 text-2xl mb-2"></i>
                        <div class="font-bold text-green-400">All Requirements Completed!</div>
                        <div class="text-sm text-green-300 mt-1">Your access code is: <span class="font-mono font-bold">3847291650</span></div>
                    </div>
                </div>
            </div>

            <!-- Code Input -->
            <div>
                <label class="block text-sm font-semibold mb-2">Enter Access Code:</label>
                <input 
                    type="text" 
                    id="accessCodeInput" 
                    class="access-code-input w-full p-3 rounded-lg focus:outline-none"
                    placeholder="Enter 10-digit code"
                    maxlength="10"
                    pattern="[0-9]*"
                    inputmode="numeric"
                >
                <button 
                    id="enterGameBtn" 
                    class="w-full mt-4 bg-gradient-to-r from-blue-500 to-blue-700 hover:from-blue-600 hover:to-blue-800 text-white font-bold py-3 px-6 rounded-lg transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
                    disabled
                >
                    <i class="fas fa-crown mr-2"></i>
                    Enter Castle Kingdom
                </button>
            </div>

            <!-- Error Message -->
            <div id="errorMessage" class="hidden mt-4 bg-red-900 border border-red-500 text-red-300 px-4 py-3 rounded-lg text-sm text-center">
                Invalid access code. Please complete all social media tasks first.
            </div>
        </div>

        <!-- Footer -->
        <div class="text-center text-xs text-slate-500">
            <p>© 2025 Sahil Castle Game. All rights reserved.</p>
            <p class="mt-1">Join our community to unlock the kingdom!</p>
        </div>
    </div>

    <!-- Registration Page (initially hidden) -->
    <div id="registrationPage" class="hidden entry-page flex flex-col items-center justify-center p-6">
        <!-- Header -->
        <div class="text-center mb-8">
            <div class="floating-castle w-32 h-32 mx-auto mb-6 bg-gradient-to-br from-purple-500 to-purple-700 rounded-3xl flex items-center justify-center shadow-2xl castle-glow">
                <i class="fas fa-user-plus text-6xl text-white"></i>
            </div>
            <h1 class="text-4xl font-bold gradient-text mb-2">Join the Kingdom</h1>
            <p class="text-slate-400 dark:text-gray-400">Create your royal account to save your progress</p>
        </div>

        <!-- Login Option -->
        <div class="w-full max-w-md mb-4">
            <div class="text-center">
                <button id="showLoginBtn" class="text-blue-400 hover:text-blue-300 text-sm underline mb-4">
                    Already have an account? Login here
                </button>
            </div>
        </div>

        <!-- Registration Form -->
        <div id="registrationForm" class="w-full max-w-md bg-slate-800 dark:bg-gray-800 rounded-lg p-6 mb-6">
            <h2 class="text-xl font-bold mb-4 text-center">🏰 Royal Registration</h2>
            
            <form id="regForm" class="space-y-4">
                <div>
                    <label class="block text-sm font-semibold mb-2">Royal Name *</label>
                    <input 
                        type="text" 
                        id="regUsername" 
                        class="w-full p-3 bg-slate-700 dark:bg-gray-700 rounded-lg border border-slate-600 dark:border-gray-600 text-white text-base focus:outline-none focus:border-blue-500"
                        placeholder="Enter your royal name"
                        required
                        maxlength="20"
                    >
                </div>

                <div>
                    <label class="block text-sm font-semibold mb-2">Email Address *</label>
                    <input 
                        type="email" 
                        id="regEmail" 
                        class="w-full p-3 bg-slate-700 dark:bg-gray-700 rounded-lg border border-slate-600 dark:border-gray-600 text-white text-base focus:outline-none focus:border-blue-500"
                        placeholder="Enter your email"
                        required
                    >
                </div>

                <div>
                    <label class="block text-sm font-semibold mb-2">Phone Number *</label>
                    <input 
                        type="tel" 
                        id="regPhone" 
                        class="w-full p-3 bg-slate-700 dark:bg-gray-700 rounded-lg border border-slate-600