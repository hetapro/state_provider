/**
 * Created by Heta on 27-12-2014.
 */
//angular.module("polls.home",[])
//
//.config(function($stateProvider, $urlRouterProvider) {

  // For any unmatched url, redirect to /state1
//  $urlRouterProvider.otherwise("/");

  // Now set up the states

//        To load dashboard.html and bind its controller
//        $stateProvider.state('main', {
//            url: '/'
////            controller: 'AppCtrl',
////            templateUrl: '/polls/index.html'
//        })
//         $stateProvider.state('main.home', {
//            url: '/home',
//            controller: 'HomeCtrl',
//            templateUrl: '/static/src/app/home/home.html'
//        })


//})

polls.controller( 'HomeCtrl',['$scope','$state','Restangular', function homeCtrl( $scope, $state, Restangular) {

      console.log("Home Ctrl is loaded");

      $scope.pageTitle = 'Polls Home Page' ;
var questions = Restangular.one("polls/questions").get().then(function (response) {
    $scope.questions=response.data;
});
        // Toggle slidebar

 }])

