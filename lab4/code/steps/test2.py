from behave import Given, When, Then
from main import get_roots

@Given(u'Calculator app is run')
def step_impl(context):
   pass

@When(u'I input "{a}", "{b}" and "{c}" to calculator')
def step_impl(context, a, b, c):
    context.result = str(get_roots(float(a), float(b), float(c)))

@Then(u'I get result "{out}"')
def step_impl(context, out):
    if (context.result == out):
        pass
    else :
        raise Exception ("Invalid roots")