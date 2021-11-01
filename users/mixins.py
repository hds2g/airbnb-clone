from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page not found"

    def test_func(self):
        # print(f"test_func: {self.request.user.is_authenticated}")
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        # print("handle_no_permission")
        return redirect("core:home")
