class OrderForm(forms.ModelForm):
 class Meta:
        model = Order
        fields = ['service', 'client', 'quantity', 'ready_by_date']
