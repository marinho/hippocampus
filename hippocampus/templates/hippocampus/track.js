(function () {
    var cname = "{{ cookie_name }}", cval = "{{ cookie_val }}", logExitUrl = "{{ log_exit_url }}";
    Hippocampus = function (cookieName, cookieVal) {
        this.cookieName = cookieName;
        this.cookieVal = cookieVal;
    };

    Hippocampus.prototype = {
        init: function() {
            if (!this.readCookie(this.cookieName)) {
                this.createCookie(this.cookieName, this.cookieVal);
                this.track('.');
            }
            window.onbeforeunload = function () {
                this.track(logExitUrl);
            };
        },

        createCookie: function(name, value) {
            // set cookie expires date one year in the future
            var date = new Date();
            date.setTime(date.getTime()+(365*24*60*60*1000));
            var expires = "; expires="+date.toGMTString();
            document.cookie = name+"="+value+expires+"; path=/";
        },

        readCookie: function(name) {
            var nameEQ = name + "=";
            var ca = document.cookie.split(';');
            for(var i=0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0)==' ') 
                    c = c.substring(1,c.length);
                if (c.indexOf(nameEQ) == 0) 
                    return c.substring(nameEQ.length,c.length);
            }
            return null;
        },

        getXHR: function() {
            if (window.XMLHttpRequest) {
                return new XMLHttpRequest();
            }
            if (window.ActiveXObject) {
                return new ActiveXObject("Microsoft.XMLHTTP");
            }
            return null;
        },

        track: function(url) {
            if (xhr = this.getXHR()) {
                xhr.open('GET', url, true);
                xhr.send(null);
            }
        }
    };
    hc = new Hippocampus("{{ cookie_name }}", "{{ cookie_val }}");
    hc.init();
})();
