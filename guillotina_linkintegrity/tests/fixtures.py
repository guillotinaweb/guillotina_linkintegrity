from guillotina import testing
import pytest


annotations = {
    'redis': None,
}


def base_settings_configurator(settings):
    if 'applications' in settings:
        settings['applications'].append('guillotina_linkintegrity')
    else:
        settings['applications'] = ['guillotina_linkintegrity']
    if annotations['redis'] is not None:
        if 'redis' not in settings:
            settings['redis'] = {}
        settings['redis']['host'] = annotations['redis'][0]
        settings['redis']['port'] = annotations['redis'][1]


testing.configure_with(base_settings_configurator)


@pytest.fixture(scope='session')
def redis():
    import pytest_docker_fixtures
    host, port = pytest_docker_fixtures.redis_image.run()
    annotations['redis'] = (host, port)
    yield host, port  # provide the fixture value
    pytest_docker_fixtures.redis_image.stop()
    annotations['redis'] = None



