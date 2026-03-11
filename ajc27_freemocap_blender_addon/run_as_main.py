from ajc27_freemocap_blender_addon.main import ajc27_run_as_main_function as _run


def ajc27_run_as_main_function(recording_path: str,
                               blend_file_path: str = "",
                               save_path: str = "",
                               config=None):
    path = blend_file_path or save_path
    if config is None:
        from ajc27_freemocap_blender_addon.data_models.parameter_models.load_parameters_config import \
            load_default_parameters_config
        config = load_default_parameters_config()
    _run(recording_path=recording_path, blend_file_path=path, config=config)
