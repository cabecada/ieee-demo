from gym.envs.registration import register

register(
    id='foo-v11',
    entry_point='gym_foo.envs:FooEnv',
)