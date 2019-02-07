# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Registered views for our record editor module."""

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template

from .permissions import need_editor_permissions


def create_editor_blueprint(app):
    """Wrapper for our blueprint to create it on demand."""
    blueprint = Blueprint(
        "invenio_records_editor",
        __name__,
        url_prefix=app.config["RECORDS_EDITOR_URL_PREFIX"],
        template_folder="templates",
        static_folder="static",
    )

    @blueprint.route("/<string:rec_type>/<int:rec_id>")
    @need_editor_permissions("editor-view")
    def index(rec_type, rec_id):
        """Render a basic view, with dummy permission editor-view."""
        return render_template(
            app.config["RECORDS_EDITOR_TEMPLATE"],
            editor_url=app.config["RECORDS_EDITOR_URL_PREFIX"],
            module_name="Invenio-Records-Editor",
            records_editor_config=app.config["RECORDS_EDITOR_CONFIG"],
        )

    return blueprint
