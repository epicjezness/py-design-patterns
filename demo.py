import logging
from typing import List, Dict

from behavioral.cor import CORBehavioralDemoService
from behavioral.mediator import MediatorBehavioralDemoService
from behavioral.observer import ObserverBehavioralDemoService
from creational.factory_method import FactoryMethodCreationalDemoService
from creational.singleton import SingletonCreationalDemoService
from structural.adapter import AdapterStructuralDemoService
from structural.decorator import DecoratorStructuralDemoService
from structural.facade import FacadeStructuralDemoService

logging.basicConfig(level=logging.DEBUG)


def _build_demo_list() -> List[Dict]:
    """
    Builds a list of available demos for the user.

    :return: Dict of available demos.
    """

    _demos = list()
    services = [FactoryMethodCreationalDemoService(), SingletonCreationalDemoService(), AdapterStructuralDemoService(),
                DecoratorStructuralDemoService(), FacadeStructuralDemoService(), CORBehavioralDemoService(),
                MediatorBehavioralDemoService(), ObserverBehavioralDemoService()]

    for x in range(0, len(services)):
        _demo = dict(idx=str(x+1), svc=services[x])
        _demos.append(_demo)

    return _demos


def _show_available_demos(_demos) -> None:
    """
    Displays all available demos.

    :param _demos: The list if demos.
    """

    print('Please select from the available demos: ')

    for _demo in _demos:
        print(f'{_demo["idx"]}: {_demo["svc"].__module__}')

    print('Enter the designated number of the demo to execute then press ENTER.')


def _get_demo_service(_demos: list, _ans: str) -> Dict:
    """
    Retrieves the demo to execute.

    :param _demos: The list of demos.
    :param _ans: The user input.
    """

    for _demo in _demos:
        if _ans == _demo['idx']:
            return _demo


if __name__ == '__main__':
    print('Welcome to Python Design Patterns Demo.')
    demos = _build_demo_list()
    _show_available_demos(demos)
    ans = input('Demo #: ')
    demo = _get_demo_service(demos, _ans=ans)

    if not demo:
        print('No demo found for given number.')

    else:
        re_trigger = True

        while re_trigger:
            svc = demo['svc']
            print(f'Demo for {svc.__module__} selected. Executing...')
            svc.execute()

            ans_2 = input('Re-trigger? (Y/n): ')

            if ans_2.lower() not in ['y', 'yes', '']:
                re_trigger = False

    print('Finished.')
