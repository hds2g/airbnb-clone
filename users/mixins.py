from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page not found"

    def test_func(self):
        # print(f"test_func: {self.request.user.is_authenticated}")
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        # print("handle_no_permission")
        return redirect("core:home")


class EmailLoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, _("Can't go there"))
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    # messages.error(self.request, "You have to Log-In")
    login_url = reverse_lazy("users:login")
