import unittest

from data import city_visit
from data import runner_util
from finder import runner as finder_runner


class CityVisitFinderRunnerTest(unittest.TestCase):
  
  def testGeneral(self):
    city_visit_finder_runner = finder_runner.CityVisitFinderRunner()
    visit_location = city_visit.VisitLocation('San Francisco')
    start_end_coordinates = (
        city_visit_finder_runner.city_visit_finder.database_connection.
        GetPoint(visit_location, 'Union Square').coordinates_starts)
    first_day, last_day = 1, 2
    day_visit_parameterss = runner_util.GetDayVisitParameterss(start_end_coordinates, first_day, last_day)
    city_visit_parameters = runner_util.GetCityVisitParameters(visit_location, day_visit_parameterss)
  
    city_visit_finder_runner.Run(city_visit_parameters)


if __name__ == '__main__':
    unittest.main()
  