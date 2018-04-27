// Gruntfile.js
module.exports = function(grunt) {
    grunt.initConfig({
        // Watch task config
        watch: {
            sass: {
                files: "blog/static/css/src/**/*.scss",
                tasks: ['sass']
            }
        },
        // SASS task config
        sass: {
            dev: {
                files: {
                    // destination         // source file
                    "blog/static/css/main.css" : "blog/static/css/src/main.scss"
                }
            }
        },
        // BrowserSync task config
        browserSync: {
            dev: {
                bsFiles: {
                    src : [
                        'blog/static/css/*.css',
                        '*.html',
                        'blog/static/js/*.js'
                    ]
                },
                options: {
                    watchTask: true,
                    proxy: "127.0.0.1:8000"
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');

    grunt.registerTask('default', ['browserSync', 'watch']);
};

