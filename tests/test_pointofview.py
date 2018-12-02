# -*- coding: utf-8 -*-

import pointofview

POV_FIRST_SINGULAR="""
When I try to analyze my own cravings, motives, actions and so forth, I surrender to a sort of retrospective imagination which feeds the analytic faculty with boundless alternatives and which causes each visualized route to fork and re-fork without end in the maddeningly complex prospect of my past.
"""
# Lolita by Vladimir Nabakov

POV_FIRST_PLURAL="""
Most of us on the boat were accomplished, and were sure we would make good wives. We knew how to cook and sew. We knew how to serve tea and arrange flowers and sit quietly on our flat wide feet for hours, saying absolutely nothing of substance at all.
"""
# The Buddha in the Attic by Julie Otsuka

POV_SECOND="""
You are not the kind of guy who would be at a place like this at this time of the morning. But here you are, and you cannot say that the terrain is entirely unfamiliar, although the details are fuzzy.
"""
# Bright Lights, Big City by Jay Mclnemey

POV_SECOND="""
While standing in his parents kitchen, you tell your boyfriend you’re leaving. You’re not going to college. You’re not buying into the schedules, the credits, or the points.  No standardized success for you.
"""

POV_THIRD="""
The family of Dashwood had long been settled in Sussex. Their estate was large, and their residence was at Norland Park, in the centre of their property, where, for many generations, they had lived in so respectable a manner as to engage the general good opinion of their surrounding acquaintance.
"""
# Sense and Sensibility by Jane Austen

POV_NONE="""
Due to pytest‘s detailed assertion introspection, only plain assert statements are used. See Getting Started for more examples.
"""
# https://docs.pytest.org/en/latest/index.html

def test_first():
    assert(pointofview.get_text_pov(POV_FIRST_SINGULAR) == pointofview.FIRST)  # nosec
    assert(pointofview.get_text_pov(POV_FIRST_PLURAL) == pointofview.FIRST)    # nosec

def test_second():
    assert(pointofview.get_text_pov(POV_SECOND) == pointofview.SECOND)         # nosec

def test_third():
    assert(pointofview.get_text_pov(POV_THIRD) == pointofview.THIRD)           # nosec

def test_none():
    assert(pointofview.get_text_pov(POV_NONE) == pointofview.NONE)               # nosec
