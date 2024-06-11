import pyrealsense2 as rs
import json

bag_name="prawa1"
bag_filename = bag_name + "BAG.bag"
output_json_filename = bag_name + "JSON.json"

def get_intrinsics_from_bag(bag_filename, output_json_filename):
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_device_from_file(bag_filename)

    profile = pipeline.start(config)

    # Pobierz profil strumienia dla kamery kolorowej i głębi
    color_stream = profile.get_stream(rs.stream.color)
    depth_stream = profile.get_stream(rs.stream.depth)

    color_intrinsics = color_stream.as_video_stream_profile().get_intrinsics()
    depth_intrinsics = depth_stream.as_video_stream_profile().get_intrinsics()

    intrinsics_data = {
        "color": {
            "width": color_intrinsics.width,
            "height": color_intrinsics.height,
            "fx": color_intrinsics.fx,
            "fy": color_intrinsics.fy,
            "cx": color_intrinsics.ppx,
            "cy": color_intrinsics.ppy,
            "coeffs": color_intrinsics.coeffs
        },
        "depth": {
            "width": depth_intrinsics.width,
            "height": depth_intrinsics.height,
            "fx": depth_intrinsics.fx,
            "fy": depth_intrinsics.fy,
            "cx": depth_intrinsics.ppx,
            "cy": depth_intrinsics.ppy,
            "coeffs": depth_intrinsics.coeffs
        }
    }

    with open(output_json_filename, 'w') as json_file:
        json.dump(intrinsics_data, json_file, indent=4)

    pipeline.stop()

    # Drukowanie parametrów do weryfikacji
    print(f"Intrinsics saved to {output_json_filename}")
    print("Color Intrinsics:")
    print(f"Width: {color_intrinsics.width}")
    print(f"Height: {color_intrinsics.height}")
    print(f"fx: {color_intrinsics.fx}")
    print(f"fy: {color_intrinsics.fy}")
    print(f"cx: {color_intrinsics.ppx}")
    print(f"cy: {color_intrinsics.ppy}")
    print(f"Distortion Coefficients: {color_intrinsics.coeffs}")

    print("\nDepth Intrinsics:")
    print(f"Width: {depth_intrinsics.width}")
    print(f"Height: {depth_intrinsics.height}")
    print(f"fx: {depth_intrinsics.fx}")
    print(f"fy: {depth_intrinsics.fy}")
    print(f"cx: {depth_intrinsics.ppx}")
    print(f"cy: {depth_intrinsics.ppy}")
    print(f"Distortion Coefficients: {depth_intrinsics.coeffs}")

# Przykład użycia
get_intrinsics_from_bag(bag_filename, output_json_filename)
