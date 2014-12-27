var polls=angular.module("polls",
            [
               'ui.router',
                'restangular'

//                'polls.home'
            ])

.config(function($stateProvider, $urlRouterProvider) {

  // For any unmatched url, redirect to /state1
//  $urlRouterProvider.otherwise("/");

  // Now set up the states

//        To load dashboard.html and bind its controller
        $stateProvider.state('main', {
            url: '/'
//            controller: 'AppCtrl',
//            templateUrl: '/polls/index.html'
        })
         $stateProvider.state('home', {
            url: '/home',
            controller: 'HomeCtrl',
            templateUrl: '/static/src/app/home/home.html'
        })


})

.controller( 'AppCtrl',['$scope','$state', function appCtrl( $scope, $state ) {

      console.log("App Ctrl is loaded");

      $scope.pageTitle = 'Polls Home Page' ;

        // Toggle slidebar

 }])


