from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField
from django.forms.widgets import *
from pages.models import *
import datetime

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['key', 'value', 'date', 'facility', 'area']
    # facility = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(),
    #                                      choices=((1, 'Rec Center'), (2, 'Clawson'), (3, 'North Quad'), (4,'All')))
    

class DatasetForm(forms.Form):
    label = forms.CharField(max_length=40)
    facility = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(), initial=('all', 'All'), 
                                         choices=(('all', 'All'), ('rec', 'Rec Center'), ('clawson', 'Clawson'), ('nq', 'North Quad')))
    area = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(), initial=('all', 'All'), 
                                         choices=(('all','All'), ('fc','Fitness Center'), ('gf', 'Group Fitness')))
    start_date = forms.DateTimeField(label="Start Date", initial=datetime.datetime.now().strftime("%Y-%m-%d"))
    end_date = forms.DateTimeField(label='End Date', initial=datetime.datetime.now().strftime("%Y-%m-%d"))
    units = forms.ChoiceField(choices = (('hour', 'Hour'), ('day', 'Day'), ('week', 'Week'), ('month', 'Month'), ('year', 'Year'), ('all', 'One Group')), label='Increment Units')
    gender = forms.ChoiceField(choices=(('all', 'All'), ('m', 'Male'), ('f', 'Female')), label='Gender')
    year = forms.MultipleChoiceField(initial=('all', 'All'), choices=(('all', 'All'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'),
                                            ('2011', '2011'), ('2010', '2010'),('2009', '2009'), ('2008', '2008'),('2007', '2007'), ('2006', '2006')))
    month = forms.MultipleChoiceField(initial=('all', 'All'), choices=(('all', 'All'), ('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'),
                                            ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'),('11', 'November'), ('12', 'December')))
    week = forms.MultipleChoiceField(initial=('all', 'All'), choices=(('all', 'All'), ('01', 'Week 1'), ('02', 'Week 2'), ('03', 'Week 3'), ('04', 'Week 4'), ('05', 'Week 5'), ('06', 'Week 6'),
                                              ('07', 'Week 7'), ('08', 'Week 8'), ('09', 'Week 9'),('10', 'Week 10'), ('11', 'Week 11'),('12', 'Week 12'),
                                              ('13', 'Week 13'), ('14', 'Week 14'), ('15', 'Week 15'), ('16', 'Week 16'), ('17', 'Week 17'),
                                              ('18', 'Week 18'), ('19', 'Week 19'), ('20', 'Week 20'), ('21', 'Week 21'), ('22', 'Week 22'),
                                              ('23', 'Week 23'), ('24', 'Week 24'), ('25', 'Week 25'), ('26', 'Week 26'), ('27', 'Week 27'),
                                              ('28', 'Week 28'), ('29', 'Week 29'), ('30', 'Week 30'), ('31', 'Week 31'), ('32', 'Week 32'),
                                              ('33', 'Week 33'), ('34', 'Week 34'), ('35', 'Week 35'), ('36', 'Week 36'), ('37', 'Week 37'),
                                              ('38', 'Week 38'), ('39', 'Week 39'), ('40', 'Week 40'), ('41', 'Week 41'), ('42', 'Week 42'),
                                              ('43', 'Week 43'), ('44', 'Week 44'), ('45', 'Week 45'), ('46', 'Week 46'), ('47', 'Week 47'),
                                              ('48', 'Week 48'), ('49', 'Week 49'), ('50', 'Week 50'), ('51', 'Week 51'), ('52', 'Week 52'),
                                              ('53', 'Week 53')))
    day_of_month = forms.MultipleChoiceField(initial=('all', 'All'), choices=(('all', 'All'), ('1', 'Day 1'), ('2', 'Day 2'), ('3', 'Day 3'), ('4', 'Day 4'), ('5', 'Day 5'), ('6', 'Day 6'),
                                                     ('7', 'Day 7'), ('8', 'Day 8'), ('9', 'Day 9'), ('10', 'Day 10'), ('11', 'Day 11'), ('12', 'Day 12'),
                                                     ('13', 'Day 13'), ('14', 'Day 14'), ('15', 'Day 15'), ('16', 'Day 16'), ('17', 'Day 17'),
                                                     ('18', 'Day 18'), ('19', 'Day 19'), ('20', 'Day 20'), ('21', 'Day 21'), ('22', 'Day 22'),
                                                     ('23', 'Day 23'), ('24', 'Day 24'), ('25', 'Day 25'), ('26', 'Day 26'), ('27', 'Day 27'),
                                                     ('28', 'Day 28'), ('29', 'Day 29'), ('30', 'Day 30'), ('31', 'Day 31')))
    day_of_week = forms.MultipleChoiceField(initial=('all', 'All'), choices=(('all', 'All'), ('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'),
                                                     ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')))

    time = forms.MultipleChoiceField(initial=('all', 'All'), choices=(('all', 'All'), ('0630', '6:30'), ('0730', '7:30'), ('0830', '8:30'), ('0930', '9:30'),
                                            ('1030', '10:30'), ('1130', '11:30'), ('1230', '12:30'), ('1330', '13:30'), ('1430', '14:30'),
                                            ('1530', '15:30'), ('1630', '16:30'), ('1730', '17:30'), ('1830', '18:30'), ('1930', '19:30'),
                                            ('2030', '20:30'), ('2130', '21:30'), ('2230', '22:30')))
    color = forms.ChoiceField(choices=(('rgb(0, 0, 0, .5)', 'Black'), ('rgb(255, 0, 0, .5)', 'Red'), ('rgb(255, 127, 0, .5)', 'Orange'), ('rgb(255, 255, 0, .5)', 'Yellow'), 
                                        ('rgb(127, 255, 0, .5)', 'Light Green'), ('rgb(0, 255, 0, .5)', 'Green'), ('rgb(0, 255, 127, .5)', 'Blue Green'),
                                        ('rgb(0, 255, 255, .5)', 'Cyan'), ('rgb(0, 0, 255, .5)', 'Blue'), ('rgb(127, 0, 255, .5)', 'Violet'), 
                                        ('rgb(255, 0, 255, .5)', 'Magenta')))

# class EditDatasetForm(forms.Form):
    # label = EditChartLabel(queryset = Graph)

class ChartForm(forms.Form):
    type = forms.ChoiceField(initial=('line', 'Line Chart'), required=True, widget=forms.RadioSelect(), choices=(('line', 'Line Chart'), ('bar', 'Bar Chart'), ('pie', 'Pie Chart'),
                                                  ('scatter', 'Scatter Plot')))

class SaveTemplateForm(forms.Form):
    name = forms.CharField()

class SelectTemplateChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.name)

class SelectTemplateForm(forms.Form):
    name = SelectTemplateChoiceField(queryset = ChartSet.objects.filter(saved=1), widget=forms.RadioSelect(), empty_label=None)

class SelectChartForm(forms.Form):
    selected_chart_id = forms.CharField()

class SelectGraphForm(forms.Form):
    selected_graph_id = forms.CharField()

class EditChartLabel(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.name)