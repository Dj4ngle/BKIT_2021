from behave import Given,When,Then
from bot2 import *

@Given("ordering food with answers in bot milk product - {a} meat and fish - {b} bakery product - {c}")
def given_answers(context,a,b,c):
    context.ans1=int(a)
    context.ans2=int(b)
    context.ans3=int(c)

@When("we form summary of check")
def make_summary(context):
    res = summary(milk,milk_price,meat_fish,meat_fish_price,bread,bread_price,context.ans1,context.ans2,context.ans3)
    context.result=res

@Then("check should be with correct price {d}")
def compare_results(context,d):
    corres= "Итоговая сумма = " + str(d)+ "\n"
    assert(context.result == corres )


