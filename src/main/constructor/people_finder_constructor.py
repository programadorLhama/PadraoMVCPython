from src.views.people_finder_view import PeopleFinderView
from src.controllers.people_finder_controller import PeopleFinderController


def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()

    person_finder_informations = people_finder_view.find_person_view()
    response = people_finder_controller.find_by_name(person_finder_informations)

    if response["success"]:
        people_finder_view.find_person_success(response["message"])
    else:
        people_finder_view.find_person_fail(response["error"])
