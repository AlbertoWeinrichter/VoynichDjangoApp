(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{303:function(n,t,o){"use strict";o.r(t),o.d(t,"showLogin",function(){return d}),o.d(t,"logout",function(){return w});var e=o(339),r=o.n(e),c=o(81),l=function(n){return new(0,o(304).default)("HnuOd4L46INOJW8G271UnFFvudbXV9KN","bitcore.eu.auth0.com",n)},f=function(){return"".concat(window.location.protocol,"//").concat(window.location.host)},d=function(n){return l(function(n){var t=r.a.v4();return Object(c.setSecret)(t),{container:n,closable:!1,auth:{responseType:"token id_token",redirectUrl:"".concat(f(),"/auth/signed-in"),params:{scope:"openid profile email",state:t}}}}(n)).show()},w=function(){return l().logout({returnTo:f()})}},586:function(n,t,o){"use strict";o.r(t);var e={mounted:function(){var n=o(81).unsetToken,t=o(303).logout;n(),t()}},r=o(21),component=Object(r.a)(e,function(){var n=this.$createElement;return(this._self._c||n)("p",[this._v("Signing off...")])},[],!1,null,null,null);t.default=component.exports}}]);