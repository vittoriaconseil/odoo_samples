odoo.define('oepetstore.Homepage', function(require) {
	"use strict";

	var core = require('web.core');
	var Widget = require('web.Widget');

	var _t = core._t;

	var QWeb = core.qweb;

	/**
	 * @author heifara
	 */
	var HomePage = Widget.extend({
		className : 'oe_petstore_homepage',
		template : "HomePageTemplate",

		init : function(parent) {
			this._super(parent);
			this.name = "Mordecai";
		},

		start : function() {
			this.$el.append("<div>Hello dear Odoo user!</div>");
			var greeting = new GreetingsWidget(this);
			greeting.appendTo(this.$el);
			console.log(this.getChildren()[0].$el);

			// QWeb.render() looks for the specified template, renders it to a
			// string and returns the result.
			// this.$el.append(QWeb.render("HomePageTemplate", {name:
			// "Klaus"}));
		},
	});

	/**
	 * @author heifara
	 */
	var GreetingsWidget = Widget.extend({
		className : 'oe_petstore_greetings',
		start : function() {
			this.$el.append("<div>We are so happy to see you again in this menu!</div>");
			this.$el.append("<button class='my_button'>Display ProductsTemplate</button>");
			this.$el.append("<hr>")
			console.log(this.getParent().$el);

			// Event after html
			var self = this;

			// Avoid this method when possible. Use the events label cf:
			// ProductWidget
			this.$(".my_button").click(function() {
				self.openProductWidget();
			});
		},

		openProductWidget : function() {
			// Exercises: Usage of QWeb in Widgets
			if (this.productWidget == null) {
				this.productWidget = new ProductWidget(this, [ "Mouse", "Keyboard" ], "blue");
				this.productWidget.on("close", this, this.closeProductWidget);
				this.productWidget.appendTo(this.$el);
			} else {
				alert("already showing!!");
			}
		},

		// not working
		closeProductWidget : function(confirm) {
			console.log(confirm);
			this.productWidget.destroy();
			this.productWidget = null;
		}

	});

	/**
	 * @author heifara
	 */
	var ProductWidget = Widget.extend({
		template : "ProductsTemplate",

		events : {
			'click button.prodButton' : function() {
				alert("Clicked!!");
				console.log(this.$el);
			},

			'click button.close_button' : function() {
				this.trigger('close', true);
			}
		},

		init : function(parent, products, color) {
			this._super(parent);
			this.products = products;
			this.color = color;
		},

		start : function() {
			// ATTENTION!!! NE MARCHE PAS SI CE CODE EST DANS LE TEMPLATE !!!!
			// ETRANGE !!!
			this.$el.append("<button class='close_button'>Close</button>");
		},

	})

	core.action_registry.add("petstore.homepage", HomePage);
});