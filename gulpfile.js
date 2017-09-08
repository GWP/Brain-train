var gulp = require('gulp');
// var gulpBrowser = require('gulp-browser');
// var babelify = require('babelify');
// var del = require('del');
// var size = require('gulp-size');


// // tasks

// gulp.task('transform', function () {
// 	var stream = gulp.src('./app/static/jsx/*.js')
// 		.pipe(gulpBrowser.browserify({transform: ['babelify']}))
// 		.pipe(gulp.dest('./app/static/scripts/js/'))
// 		.pipe(size());

// 	return stream;
// });

// gulp.task('del', function () {
//     return del(['./app/static/scripts/js'])
// });

// gulp.task('default', ['del'], function() {
//   gulp.start('transform');
//   gulp.watch('./app/static/jsx/*.js', ['transform']);
// });

var babelify = require('babelify');
var browserify = require('browserify');
var buffer = require('vinyl-buffer');
var source = require('vinyl-source-stream');
var uglify = require('gulp-uglify');

gulp.task('default', function () {
    var bundler = browserify('./app/static/jsx/*.js');
    bundler.transform(babelify);

    bundler.bundle()
        .on('error', function (err) { console.error(err); })
        .pipe(source('./app/static/jsx/*.js'))
        .pipe(buffer())
        .pipe(uglify()) // Use any gulp plugins you want now
        .pipe(gulp.dest('./app/static/scripts/js/'));
});
