import cas.registration.util as util
import numpy as np
import transformations

np.set_printoptions(suppress=True)
from sklearn.neighbors import NearestNeighbors


def paired_points_matching(source, target):
    """

    :param source:
    :param target:
    :return:
        T: 4x4 transformation matrix mapping source onto target
        R: 3x3 rotation matrix part of T
        t: 1x3 translation vector part of T
    """
    assert source.shape == target.shape
    T = np.eye(4)
    R = np.eye(3)
    t = np.zeros((1, 3))

    return T, R, t


def find_nearest_neighbor(src, dst):

   pass


def icp(source, target, init_pose=None, max_iterations=10, tolerance=0.0001):
    T = np.eye(4)
    distances = 0
    error = 0

    return T, distances, error


def get_initial_pose(template_points, target_points):
    return transformations.rotation_matrix(1.5, [1, 0, 0])


if __name__ == "__main__":
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    target_points = util.read_data('../../data/registration/TargetPoints.csv')
    print(target_points)

    template_points = util.read_data('../../data/registration/TemplatePoints.csv')
    print(template_points)

    T_rot_x = get_initial_pose(template_points, target_points)
    T, d, error = icp(template_points, target_points, init_pose=T_rot_x)

    template_points_T = util.make_homogenous(template_points)
    template_points_T = np.dot(T, template_points_T.T).T[:, :3]

    print(template_points_T)

    print(T)

    print(error)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    sample_choice = np.random.choice(target_points.shape[0], 1000)
    # print(sample_choice)
    samples = target_points[sample_choice, :]
    ax.scatter(samples[:, 0], samples[:, 1], samples[:, 2], c='b', marker='.')
    # ax.scatter(template_points[:, 0], template_points[:, 1], template_points[:, 2], c='g', marker='x')
    ax.scatter(template_points_T[:, 0], template_points_T[:, 1], template_points_T[:, 2], c='r', marker='x')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # plt.axis([-3, 3, -3, 3])
    plt.axis('equal')
    plt.show()