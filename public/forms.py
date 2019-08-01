from django import forms


class YelpSearchForm(forms.Form):
    password = forms.CharField(label='Password', max_length=250, help_text='REQUIRED! Yes, those who signed up will receive a\
     passcode. Message u/YoomamaFTW on reddit to sign up.', required=True)
    term = forms.CharField(label='Term/Keyword: ', max_length=250, required=False,
                           help_text='You can send multiple terms in this format: term, term  OR term,term')
    location = forms.CharField(label='Location: ', max_length=250, required=True,
                               help_text='REQUIRED! This string indicates the geographic area to be used when '
                                         'searching for businesses. Examples: "New York City", "NYC", "350 5th Ave,'
                                         ' New York, NY 10118". Businesses returned in the response may not be '
                                         'strictly within the specified location.')
    radius = forms.IntegerField(label='Radius: ', required=False, help_text='The value is in meters. Do not type in '
                                                                            'units. Only numbers')
    categories = forms.CharField(label='Categories: ', required=False,
                                 help_text='https://www.yelp.com/developers/documentation/v3/all_category_list '
                                           'for a list of supported categories')
    price = forms.CharField(label='Price: ', required=False,
                            help_text='Pricing levels to filter the search result with: 1 = $, 2 = $$, 3 = $$$, 4 = '
                                      '$$$$. The price filter can be a list of comma delimited pricing levels. For '
                                      'example, "1, 2, 3" will filter the results to show the ones that are $, $$, or '
                                      '$$$.')
    open_now = forms.BooleanField(label='Open Now: ', required=False,
                                  help_text='Default to false. When set to true, only return the businesses open now. '
                                            'Notice that open_at and open_now cannot be used together.')
