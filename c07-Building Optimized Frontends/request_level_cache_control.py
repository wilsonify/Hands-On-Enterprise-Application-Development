from bugzot.application import app, db
from bugzot.models import User
from flask.views import MethodView
from flask import render_template, session, request, make_response


class UserListView(MethodView):
    """
    User list view for displaying user data in admin panel.
    The user list view is responsible for rendering the table of users that
    are registered    in the application.
    """

    def get(self):
        """
        HTTP GET handler.
        """
        page = request.args.get('next_page', 1)  # get the page number to be displayed
        users = User.query.paginate(page, 20, False)
        total_records = users.total
        user_records = users.items
        resp = make_response(
            render_template(
                'admin/user_list.html',
                users=user_records,
                next_page=page + 1
            ))
        resp.cache_control.public = False
        return resp
