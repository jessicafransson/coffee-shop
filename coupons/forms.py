from django import forms
from coupons.models import Coupon
from tempus_dominus.widgets import DateTimePicker


class CouponApplyForm(forms.Form):
    code = forms.CharField()

    class Meta:
        model = Coupon
        fields = ['code']

    def __init__(self, *args, **kwargs):
        super(CouponApplyForm, self).__init__(*args, **kwargs)
        self.fields['code'].label = ""


class CouponForm(forms.ModelForm):

    class Meta:
        model = Coupon
        fields = ('code', 'valid_from', 'valid_to', 'discount', 'active')

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        self.fields['code'].label = "Discount Code "
        self.fields['valid_from'].label = "Valid From  "
        self.fields['valid_to'].label = "Valid To  "
        self.fields['discount'].label = "Discount Percentage "
        self.fields['valid_from'].widget.attrs['class'] = \
            'form-control datetimepicker-input'
        self.fields['valid_from'].widget = DateTimePicker()
        self.fields['valid_to'].widget.attrs['class'] = \
            'form-control datetimepicker-input'
        self.fields['valid_to'].widget = DateTimePicker()
