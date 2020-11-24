import unittest
from unittest.mock import patch
from TDD_organized_lesson.AlertCreators.camera import Camera
from TDD_organized_lesson.security_system import SecuritySystem


class CameraTest(unittest.TestCase):

    def setUp(self):
        self.camera = Camera("Camera1", ["backyard", "outside"])

        self.connectedCamera = Camera("Camera2", ["backyard", "outside"])
        system = SecuritySystem()  
        self.connectedCamera.security_system = system

        

    def test_isConnected_securitySystemNotNone_true(self):
        # setUp
        # set up everything you need to run the test

        system = SecuritySystem()  
        self.camera.security_system = system

        self.assertTrue(self.camera.is_connected())

    @patch.object(SecuritySystem, 'createAlert')
    def test_createAlert_humanOutside2_systemCreateAlert(self, system_create_alert_mock):
        self.connectedCamera.create_alert("outside", "human", 2)
        system_create_alert_mock.assert_called_once()


    def test_detectMovement_nightTimeNightMode_createsAlert(self):
        pass