odoo.define('oepetstore.tinymce', function(require) {
	"use strict";

	var core = require('web.core');
	var session = require('web.session');
	var Model = require('web.DataModel');
	var common = require('web.form_common');
	var base = require('web_editor.base');
	var editor = require('web_editor.editor');
	var summernote = require('web_editor.summernote');
	var transcoder = require('web_editor.transcoder');
	var backend = require('web_editor.backend');

	var QWeb = core.qweb;
	var _t = core._t;

	/**
	 * FieldTextHtml Widget Intended for FieldText widgets meant to display HTML
	 * content. This widget will instantiate an iframe with the editor
	 * summernote improved by odoo
	 */
	var widget = common.AbstractField.extend(common.ReinitializeFieldMixin);

	var FieldTextTinyMCE = widget.extend({
		template : 'oepetstore.tinymce',

		start : function() {
			console.log("start");
			var self = this;
			this.on('change:effective_readonly', this, function() {
			});
		},
	});

	core.form_widget_registry.add('tinymce', FieldTextTinyMCE);

	return {
		FieldTextTinyMCE : FieldTextTinyMCE,
	}

});