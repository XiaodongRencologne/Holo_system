import enum
import pydantic
class CmdPointingCorrection(pydantic.BaseModel):
    SystematicErrorModelSpemOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Systematic error model (SPEM) on')]
    TiltmeterCorrectionOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Tiltmeter correction on')]
    LinearSensorCorrectionOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Linear sensor correction on')]
    RFRefractionCorrectionOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='RF refraction correction on')]
    class Config:
        populate_by_name = True

class CmdSectorScanParameters(pydantic.BaseModel):
    StartingPositionAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='Starting position Azimuth')]
    EndPositionAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='End position Azimuth')]
    LineDistanceAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='Line distance Azimuth')]
    ScanVelocityAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='Scan velocity Azimuth')]
    StartingPositionElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='Starting position Elevation')]
    EndPositionElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='End position Elevation')]
    LineDistanceElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='Line distance Elevation')]
    ScanVelocityElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='Scan velocity Elevation')]
    PositionWindowAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='Position Window Azimuth')]
    PositionWindowElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='Position Window Elevation')]
    class Config:
        populate_by_name = True

class CmdSPEMParameter(pydantic.BaseModel):
    ParameterIA: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter IA')]
    ParameterIE: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter IE')]
    ParameterTFC: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter TFC')]
    ParameterTF: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter TF')]
    ParameterTFS: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter TFS')]
    ParameterAN: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter AN')]
    ParameterAW: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter AW')]
    ParameterCA: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter CA')]
    ParameterNPAE: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter NPAE')]
    ParameterNRX: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter NRX')]
    ParameterNRY: pydantic.typing.Annotated[float, pydantic.Field(alias='Parameter NRY')]
    class Config:
        populate_by_name = True

class CmdStarTrackTransfer(pydantic.BaseModel):
    Name: str
    RightAscension: pydantic.typing.Annotated[float, pydantic.Field(alias='Right Ascension')]
    Declination: float
    class Config:
        populate_by_name = True

class CmdTimePositionOffsetTransfer(pydantic.BaseModel):
    TimeOffset: pydantic.typing.Annotated[float, pydantic.Field(alias='Time Offset')]
    AzimuthOffset: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth Offset')]
    ElevationOffset: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation Offset')]
    class Config:
        populate_by_name = True

class CmdTimePositionTransfer(pydantic.BaseModel):
    LastUploadName: pydantic.typing.Annotated[str, pydantic.Field(alias='Last Upload Name')]
    LastUploadTime: pydantic.typing.Annotated[str, pydantic.Field(alias='Last Upload Time')]
    LastUploadTotalEntries: pydantic.typing.Annotated[int, pydantic.Field(alias='Last Upload Total Entries')]
    LastUploadValidEntries: pydantic.typing.Annotated[int, pydantic.Field(alias='Last Upload Valid Entries')]
    LastUploadInvalidEntries: pydantic.typing.Annotated[int, pydantic.Field(alias='Last Upload Invalid Entries')]
    class Config:
        populate_by_name = True

class CmdTwoLineTransfer(pydantic.BaseModel):
    NameOfSpacecraft: pydantic.typing.Annotated[str, pydantic.Field(alias='Name of Spacecraft')]
    Line1: pydantic.typing.Annotated[str, pydantic.Field(alias='Line 1')]
    Line2: pydantic.typing.Annotated[str, pydantic.Field(alias='Line 2')]
    AOSTime: pydantic.typing.Annotated[float, pydantic.Field(alias='AOS Time')]
    AOSAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='AOS Azimuth')]
    AOSElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='AOS Elevation')]
    LOSTime: pydantic.typing.Annotated[float, pydantic.Field(alias='LOS Time')]
    LOSAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='LOS Azimuth')]
    LOSElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='LOS Elevation')]
    MAXTime: pydantic.typing.Annotated[float, pydantic.Field(alias='MAX Time')]
    MAXAzimuth: pydantic.typing.Annotated[float, pydantic.Field(alias='MAX Azimuth')]
    MAXElevation: pydantic.typing.Annotated[float, pydantic.Field(alias='MAX Elevation')]
    class Config:
        populate_by_name = True

class CmdWeatherStation(pydantic.BaseModel):
    Time: float
    Year: int
    Temperature: float
    RelativeHumidity: float
    AirPressure: float
    class Config:
        populate_by_name = True

class ThirdAxisModeEnum(enum.IntEnum):
    Stop = 0
    Preset = 1
    Rate = 2
    SurvivalMode = 3
    Stow = 4

class Status3rdAxis(pydantic.BaseModel):
    ThirdAxisMode: pydantic.typing.Annotated[ThirdAxisModeEnum, pydantic.Field(alias='3rd axis Mode')]
    ThirdAxisCommandedPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='3rd axis commanded position')]
    ThirdAxisCurrentPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='3rd axis current position')]
    ThirdAxisComputerDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd axis computer disabled')]
    ThirdAxisAxisDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd axis axis disabled')]
    ThirdAxisAxisInStop: pydantic.typing.Annotated[bool, pydantic.Field(alias='3rd axis axis in stop')]
    ThirdAxisBrakesReleased: pydantic.typing.Annotated[bool, pydantic.Field(alias='3rd axis brakes released')]
    ThirdAxisStopAtLCP: pydantic.typing.Annotated[bool, pydantic.Field(alias='3rd axis stop at LCP')]
    ThirdAxisPowerOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='3rd axis power on')]
    ThirdAxisCCWLimit: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd axis CCW limit')]
    ThirdAxisCWLimit: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd axis CW limit')]
    ThirdAxisSummaryFault: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd axis summary fault')]
    class Config:
        populate_by_name = True

class StatusDetailedFaults(pydantic.BaseModel):
    PLCCommunication: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC Communication')]
    EStop1ServoDriveCabinet: pydantic.typing.Annotated[int, pydantic.Field(alias='EStop 1 - Servo Drive Cabinet')]
    EStop4AzMoveable: pydantic.typing.Annotated[int, pydantic.Field(alias='EStop 4 - Az Moveable')]
    EStop6AZFixed: pydantic.typing.Annotated[int, pydantic.Field(alias='EStop 6 - AZ Fixed')]
    EStopPCU: pydantic.typing.Annotated[int, pydantic.Field(alias='E-Stop PCU')]
    EStopDevice: pydantic.typing.Annotated[int, pydantic.Field(alias='E-Stop Device')]
    PLCGeneralSafe: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Safe')]
    PLCGeneralPowerFailureLatched: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Power Failure (latched)')]
    PLCGeneralLightningSurgeArrester: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Lightning Surge Arrester')]
    PLCGeneralPowerFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Power Failure')]
    PLCGeneral24VPowerFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - 24V Power Failure')]
    PLCGeneralBreakerFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Breaker Failure')]
    PLCGeneralCabinetOverTemperature: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Cabinet Over-Temperature')]
    PLCGeneralACUIFError: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - ACU IF Error')]
    PLCGeneralProfinetError: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Profinet Error')]
    PLCGeneralCabinetUnderTemperature: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Cabinet Under-Temperature')]
    PLCGeneralAmbientTemperatureTooLow: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Ambient-Temperature too low')]
    PLCGeneralComovingShieldRemoved: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Comoving Shield removed')]
    PLCGeneralDrivePowerOff: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Drive Power Off')]
    PLCGeneralKeySwitchSafeOverride: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Key Switch Safe Override')]
    PLCGeneralKeySwitchBypassEmergencyLimits: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Key Switch Bypass Emergency Limits')]
    PLCGeneralPCUOperation: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - PCU Operation')]
    PLCGeneralWarnHornSounding: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Warn Horn sounding')]
    PLCGeneralWarnHornPassive: pydantic.typing.Annotated[int, pydantic.Field(alias='PLC General - Warn Horn passive')]
    AzEncoderFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Encoder Failure')]
    AzRoundSwitchFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Round Switch Failure')]
    AzSecondEmergencyLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Second Emergency Limit Up/CW')]
    AzEmergencyLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Emergency Limit Up/CW')]
    AzLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Limit Up/CW')]
    AzPreLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - PreLimit Up/CW')]
    AzPreLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - PreLimit Down/CCW')]
    AzLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Limit Down/CCW')]
    AzEmergencyLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Emergency Limit Down/CCW')]
    AzSecondEmergencyLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Second Emergency Limit Down/CCW')]
    AzSoftLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Soft-Limit Up/CW')]
    AzSoftPreLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Soft-PreLimit Up/CW')]
    AzSoftPreLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Soft-PreLimit Down/CCW')]
    AzSoftLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Soft-Limit Down/CCW')]
    AzTachoFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Tacho Failure')]
    AzACUImmobile: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - ACU immobile')]
    AzCANBusFailureAmplifier1: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - CAN bus failure Amplifier 1')]
    AzCANBusFailureAmplifier2: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - CAN bus failure Amplifier 2')]
    AzComputerDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Computer Disabled')]
    AzAxisDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Axis Disabled')]
    AzFirstEmergencyLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - First Emergency Limit UpCW')]
    AzSecondEmergencyLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Second Emergency Limit UpCW')]
    AzFirstEmergencyLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - First Emergency Limit DownCCW')]
    AzSecondEmergencyLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Second Emergency Limit DownCCW')]
    AzServoFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Servo Failure')]
    AzMotionError: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Motion Error')]
    AzBrake1Failure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Brake1 Failure')]
    AzBrake2Failure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Brake2 Failure')]
    AzBreakerFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Breaker Failure')]
    AzAmplifier1Failure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Amplifier1 Failure')]
    AzAmplifier2Failure: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Amplifier2 Failure')]
    AzMotor1OverTemp: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Motor1 OverTemp')]
    AzMotor2OverTemp: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Motor2 OverTemp')]
    AzAux1ModeSelected: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Aux1 Mode Selected')]
    AzAux2ModeSelected: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Aux2 Mode Selected')]
    AzOverspeed: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Overspeed')]
    AzAmplifierPowerCylceInterlock: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Amplifier Power Cylce Interlock')]
    AzRegenResistor1OverTemp: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Regen. Resistor1 OverTemp')]
    AzRegenResistor2OverTemp: pydantic.typing.Annotated[int, pydantic.Field(alias='Az - Regen. Resistor2 OverTemp')]
    ElEncoderFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Encoder Failure')]
    ElEmergencyLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Emergency Limit Up/CW')]
    ElLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Limit Up/CW')]
    ElPreLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - PreLimit Up/CW')]
    ElPreLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - PreLimit Down/CCW')]
    ElLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Limit Down/CCW')]
    ElEmergencyLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Emergency Limit Down/CCW')]
    ElSoftLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Soft-Limit Up/CW')]
    ElSoftPreLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Soft-PreLimit Up/CW')]
    ElSoftPreLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Soft-PreLimit Down/CCW')]
    ElSoftLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Soft-Limit Down/CCW')]
    ElTachoFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Tacho Failure')]
    ElACUImmobile: pydantic.typing.Annotated[int, pydantic.Field(alias='El - ACU immobile')]
    ElCANBusFailureAmplifier1: pydantic.typing.Annotated[int, pydantic.Field(alias='El - CAN bus failure Amplifier 1')]
    ElComputerDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Computer Disabled')]
    ElAxisDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Axis Disabled')]
    ElFirstEmergencyLimitUpCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - First Emergency Limit UpCW')]
    ElFirstEmergencyLimitDownCCW: pydantic.typing.Annotated[int, pydantic.Field(alias='El - First Emergency Limit DownCCW')]
    ElServoFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Servo Failure')]
    ElMotionError: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Motion Error')]
    ElBrake1Failure: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Brake1 Failure')]
    ElBreakerFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Breaker Failure')]
    ElAmplifier1Failure: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Amplifier1 Failure')]
    ElMotor1OverTemp: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Motor1 OverTemp')]
    ElOverspeed: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Overspeed')]
    ElAmplifierPowerCylceInterlock: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Amplifier Power Cylce Interlock')]
    ElRegenResistor1OverTemp: pydantic.typing.Annotated[int, pydantic.Field(alias='El - Regen. Resistor1 OverTemp')]
    GeneralACUFanFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='General ACU fan failure')]
    GeneralACUOverTemperature: pydantic.typing.Annotated[int, pydantic.Field(alias='General ACU over temperature')]
    GeneralTimeError: pydantic.typing.Annotated[int, pydantic.Field(alias='General Time Error')]
    class Config:
        populate_by_name = True

class AzimuthTorqueBiasModeEnum(enum.IntEnum):
    Off = 0
    ConstantTorqueBias = 1
    FullTorqueBias = 2

class ElevationTorqueBiasModeEnum(enum.IntEnum):
    Off = 0
    ConstantTorqueBias = 1
    FullTorqueBias = 2

class ThirdAxisTorqueBiasModeEnum(enum.IntEnum):
    Off = 0
    ConstantTorqueBias = 1
    FullTorqueBias = 2

class SpeedEnum(enum.IntEnum):
    Low = 0
    High = 1

class TrackingStatusEnum(enum.IntEnum):
    NoTracking = 0
    ProgramTrack = 1
    AutoTrack = 2
    CombinedAutoTrack = 3

class AutotrackStatusEnum(enum.IntEnum):
    Inactive = 0
    StandardLockOn = 1
    StandardBackup = 2
    CombinedLockOn = 3
    CombinedBackup = 4

class StatusExtra8100(pydantic.BaseModel):
    AzimuthPositionCommand: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth position command')]
    AzimuthCurrentAcceleration: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth current acceleration')]
    AzimuthCombinedAutotrackIntegrationFactor: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth Combined Autotrack Integration Factor')]
    AzimuthTorqueBiasMode: pydantic.typing.Annotated[AzimuthTorqueBiasModeEnum, pydantic.Field(alias='Azimuth torque bias mode')]
    AzimuthOvercurrentMotor1: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth overcurrent motor 1')]
    AzimuthOvercurrentMotor2: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth overcurrent motor 2')]
    AzimuthOvercurrentMotor3: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth overcurrent motor 3')]
    AzimuthOvercurrentMotor4: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth overcurrent motor 4')]
    AzimuthOscillationStatus: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth oscillation status')]
    AzimuthOscillationWarning: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth oscillation warning')]
    AzimuthOscillationFailue: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth oscillation failue')]
    AzimuthProfilerActive: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth profiler active')]
    AzimuthProfilerRunning: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth profiler running')]
    AzimuthInterlockAlarm: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth interlock alarm')]
    AzimuthTorque: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth torque')]
    ElevationPositionCommand: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation position command')]
    ElevationCurrentAcceleration: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation current acceleration')]
    ElevationCombinedAutotrackIntegrationFactor: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation Combined Autotrack Integration Factor')]
    ElevationTorqueBiasMode: pydantic.typing.Annotated[ElevationTorqueBiasModeEnum, pydantic.Field(alias='Elevation torque bias mode')]
    ElevationOvercurrentMotor1: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation overcurrent motor 1')]
    ElevationOvercurrentMotor2: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation overcurrent motor 2')]
    ElevationOvercurrentMotor3: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation overcurrent motor 3')]
    ElevationOvercurrentMotor4: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation overcurrent motor 4')]
    ElevationOscillationStatus: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation oscillation status')]
    ElevationOscillationWarning: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation oscillation warning')]
    ElevationOscillationFailue: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation oscillation failue')]
    ElevationProfilerActive: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation profiler active')]
    ElevationProfilerRunning: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation profiler running')]
    ElevationInterlockAlarm: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation interlock alarm')]
    ElevationTorque: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation torque')]
    ElevationStowPosition: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation stow position')]
    ElevationStowStatus: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation stow status')]
    ElevationTrue: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation true')]
    ThirdAxisCurrentAcceleration: pydantic.typing.Annotated[float, pydantic.Field(alias='3rd Axis current acceleration')]
    ThirdAxisTorqueBiasMode: pydantic.typing.Annotated[ThirdAxisTorqueBiasModeEnum, pydantic.Field(alias='3rd Axis torque bias mode')]
    ThirdAxisOvercurrentMotor1: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd Axis overcurrent motor 1')]
    ThirdAxisOvercurrentMotor2: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd Axis overcurrent motor 2')]
    ThirdAxisOscillationStatus: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd Axis oscillation status')]
    ThirdAxisOscillationWarning: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd Axis oscillation warning')]
    ThirdAxisOscillationFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd Axis oscillation failure')]
    ThirdAxisProfilerActive: pydantic.typing.Annotated[bool, pydantic.Field(alias='3rd Axis profiler active')]
    ThirdAxisProfilerRunning: pydantic.typing.Annotated[bool, pydantic.Field(alias='3rd Axis profiler running')]
    ThirdAxisInterlockAlarm: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd Axis interlock alarm')]
    ThirdAxisTorque: pydantic.typing.Annotated[float, pydantic.Field(alias='3rd Axis torque')]
    Speed: SpeedEnum
    GreenMode: pydantic.typing.Annotated[bool, pydantic.Field(alias='Green Mode')]
    TrackingStatus: pydantic.typing.Annotated[TrackingStatusEnum, pydantic.Field(alias='Tracking Status')]
    AutotrackStatus: pydantic.typing.Annotated[AutotrackStatusEnum, pydantic.Field(alias='Autotrack Status')]
    SplineStatus: pydantic.typing.Annotated[int, pydantic.Field(alias='Spline Status')]
    CommandingQuality: pydantic.typing.Annotated[int, pydantic.Field(alias='Commanding Quality')]
    GeneralInterlockAlarm: pydantic.typing.Annotated[int, pydantic.Field(alias='General interlock alarm')]
    QtyOfUsedProgramTrackStackPositions: pydantic.typing.Annotated[int, pydantic.Field(alias='Qty of used program track stack positions')]
    QtyOfFreeProgramTrackStackPositions: pydantic.typing.Annotated[int, pydantic.Field(alias='Qty of free program track stack positions')]
    TimeToPosition: float
    TimeStampCommand: pydantic.typing.Annotated[float, pydantic.Field(alias='Time Stamp Command')]
    AzimuthNormalizedPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth normalized position')]
    AzimuthCanBusFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth can bus failure')]
    ElevationCanBusFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation can bus failure')]
    ThirdAxisCanBusFailure: pydantic.typing.Annotated[int, pydantic.Field(alias='3rd axis can bus failure')]
    class Config:
        populate_by_name = True

class AzimuthModeEnum(enum.IntEnum):
    Stop = 0
    Preset = 1
    ProgramTrack = 2
    Rate = 3
    SurvivalMode = 4
    Stow = 5
    StarTrack = 6
    SectorScan = 7

class ElevationModeEnum(enum.IntEnum):
    Stop = 0
    Preset = 1
    ProgramTrack = 2
    Rate = 3
    SurvivalMode = 4
    Stow = 5
    StarTrack = 6
    SectorScan = 7

class ElevationStowPinsStatusEnum(enum.IntEnum):
    NotAvailable = 0
    AnyMoving = 1
    AllInserted = 2
    AllRetracted = 3
    Failure = 4

class StatusGeneral8100(pydantic.BaseModel):
    Time: float
    Year: int
    AzimuthMode: pydantic.typing.Annotated[AzimuthModeEnum, pydantic.Field(alias='Azimuth Mode')]
    AzimuthCommandedPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth commanded position')]
    AzimuthCurrentPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth current position')]
    AzimuthCurrentVelocity: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth current velocity')]
    AzimuthAveragePositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth average position error')]
    AzimuthPeakPositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth peak position error')]
    AzimuthComputerDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth computer disabled')]
    AzimuthAxisDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth axis disabled')]
    AzimuthAxisInStop: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth axis in stop')]
    AzimuthBrakesReleased: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth brakes released')]
    AzimuthStopAtLCP: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth stop at LCP')]
    AzimuthPowerOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth power on')]
    AzimuthCCWLimit: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth CCW limit')]
    AzimuthCWLimit: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth CW limit')]
    AzimuthSummaryFault: pydantic.typing.Annotated[int, pydantic.Field(alias='Azimuth summary fault')]
    ElevationMode: pydantic.typing.Annotated[ElevationModeEnum, pydantic.Field(alias='Elevation Mode')]
    ElevationCommandedPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation commanded position')]
    ElevationCurrentPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation current position')]
    ElevationCurrentVelocity: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation current velocity')]
    ElevationAveragePositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation average position error')]
    ElevationPeakPositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation peak position error')]
    ElevationComputerDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation computer disabled')]
    ElevationAxisDisabled: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation axis disabled')]
    ElevationAxisInStop: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation axis in stop')]
    ElevationBrakesReleased: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation brakes released')]
    ElevationAxisInStowPosition: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation axis in stow position')]
    ElevationStowPinsStatus: pydantic.typing.Annotated[ElevationStowPinsStatusEnum, pydantic.Field(alias='Elevation stow pins - status')]
    ElevationStopAtLCP: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation stop at LCP')]
    ElevationPowerOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation power on')]
    ElevationCCWLimit: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation CCW limit')]
    ElevationCWLimit: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation CW limit')]
    ElevationSummaryFault: pydantic.typing.Annotated[int, pydantic.Field(alias='Elevation summary fault')]
    PCUOperation: pydantic.typing.Annotated[int, pydantic.Field(alias='PCU Operation')]
    ATLockOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='AT Lock On')]
    Remote: bool
    QtyOfFreeProgramTrackStackPositions: pydantic.typing.Annotated[int, pydantic.Field(alias='Qty of free program track stack positions')]
    class Config:
        populate_by_name = True

class StatusPointingCorrection(pydantic.BaseModel):
    Time: float
    Year: int
    SystematicErrorModelSpemOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Systematic error model (SPEM) on')]
    TiltmeterCorrectionOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Tiltmeter correction on')]
    LinearSensorCorrectionOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Linear sensor correction on')]
    RFRefractionCorrectionOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='RF refraction correction on')]
    Spare4: pydantic.typing.Annotated[bool, pydantic.Field(alias='Spare 4')]
    Spare5: pydantic.typing.Annotated[bool, pydantic.Field(alias='Spare 5')]
    Spare6: pydantic.typing.Annotated[bool, pydantic.Field(alias='Spare 6')]
    Spare7: pydantic.typing.Annotated[bool, pydantic.Field(alias='Spare 7')]
    Spare8: pydantic.typing.Annotated[bool, pydantic.Field(alias='Spare 8')]
    Spare9: pydantic.typing.Annotated[bool, pydantic.Field(alias='Spare 9')]
    SPEMCorrectionAZ: pydantic.typing.Annotated[float, pydantic.Field(alias='SPEM correction AZ')]
    SPEMCorrectionEL: pydantic.typing.Annotated[float, pydantic.Field(alias='SPEM correction EL')]
    TiltmeterCorrectionAZ: pydantic.typing.Annotated[float, pydantic.Field(alias='Tiltmeter correction AZ')]
    TiltmeterCorrectionEL: pydantic.typing.Annotated[float, pydantic.Field(alias='Tiltmeter correction EL')]
    LinearSensorCorrectionAZ: pydantic.typing.Annotated[float, pydantic.Field(alias='Linear sensor correction AZ')]
    LinearSensorCorrectionEL: pydantic.typing.Annotated[float, pydantic.Field(alias='Linear sensor correction EL')]
    RFRefractionCorrectionAZ: pydantic.typing.Annotated[float, pydantic.Field(alias='RF refraction correction AZ')]
    RFRefractionCorrectionEL: pydantic.typing.Annotated[float, pydantic.Field(alias='RF refraction correction EL')]
    class Config:
        populate_by_name = True

class AzimuthModeEnum(enum.IntEnum):
    Stop = 0
    Preset = 1
    ProgramTrack = 2
    Rate = 3
    SurvivalMode = 4
    Stow = 5
    StarTrack = 6
    SectorScan = 7

class ElevationModeEnum(enum.IntEnum):
    Stop = 0
    Preset = 1
    ProgramTrack = 2
    Rate = 3
    SurvivalMode = 4
    Stow = 5
    StarTrack = 6
    SectorScan = 7

class BoresightModeEnum(enum.IntEnum):
    Stop = 0
    Preset = 1
    Rate = 2
    SurvivalMode = 3
    Stow = 4

class StatusSATPDetailed8100(pydantic.BaseModel):
    Time: float
    Year: int
    AzimuthMode: pydantic.typing.Annotated[AzimuthModeEnum, pydantic.Field(alias='Azimuth mode')]
    AzimuthCommandedPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth commanded position')]
    AzimuthCurrentPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth current position')]
    AzimuthCurrentVelocity: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth current velocity')]
    AzimuthAveragePositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth average position error')]
    AzimuthPeakPositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Azimuth peak position error')]
    AzimuthComputerDisabled: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth computer disabled')]
    AzimuthAxisDisabled: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth axis disabled')]
    AzimuthAxisInStop: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth axis in stop')]
    AzimuthBrakesReleased: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth brakes released')]
    AzimuthStopAtLCP: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth stop at LCP')]
    AzimuthPowerOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth power on')]
    AzimuthCCWLimit2NdEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CCW limit: 2nd emergency')]
    AzimuthCCWLimitEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CCW limit: emergency')]
    AzimuthCCWLimitOperating: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CCW limit: operating')]
    AzimuthCCWLimitPreLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CCW limit: pre-limit')]
    AzimuthCCWLimitOperatingAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CCW limit: operating (ACU software limit)')]
    AzimuthCCWLimitPreLimitAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CCW limit: pre-limit (ACU software limit)')]
    AzimuthCWLimitPreLimitAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CW limit: pre-limit (ACU software limit)')]
    AzimuthCWLimitOperatingAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CW limit: operating (ACU software limit)')]
    AzimuthCWLimitPreLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CW limit: pre-limit')]
    AzimuthCWLimitOperating: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CW limit: operating')]
    AzimuthCWLimitEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CW limit: emergency')]
    AzimuthCWLimit2NdEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CW limit: 2nd emergency')]
    AzimuthSummaryFault: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth summary fault')]
    AzimuthServoFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth servo failure')]
    AzimuthMotionError: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth motion error')]
    AzimuthBrake1Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth brake 1 failure')]
    AzimuthBrake2Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth brake 2 failure')]
    AzimuthBreakerFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth breaker failure')]
    AzimuthAmplifier1Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth amplifier 1 failure')]
    AzimuthAmplifier2Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth amplifier 2 failure')]
    AzimuthMotor1Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth motor 1 overtemperature')]
    AzimuthMotor2Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth motor 2 overtemperature')]
    AzimuthAUX1ModeSelected: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth AUX 1 mode selected')]
    AzimuthAUX2ModeSelected: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth AUX 2 mode selected')]
    AzimuthOverspeed: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth overspeed')]
    AzimuthAmplifierPowerCylceInterlock: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth amplifier power cylce interlock')]
    AzimuthRegenerationResistor1Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth regeneration resistor 1 overtemperature')]
    AzimuthRegenerationResistor2Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth regeneration resistor 2 overtemperature')]
    AzimuthCANBusAmplifier1CommunicationFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CAN bus amplifier 1 communication failure')]
    AzimuthCANBusAmplifier2CommunicationFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth CAN bus amplifier 2 communication failure')]
    AzimuthEncoderFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth encoder failure')]
    AzimuthOscillationWarning: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth oscillation warning')]
    AzimuthOscillationAlarm: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth oscillation alarm')]
    AzimuthTachoFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth tacho failure')]
    AzimuthImmobile: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth immobile')]
    AzimuthOvercurrentMotor1: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth overcurrent motor 1')]
    AzimuthOvercurrentMotor2: pydantic.typing.Annotated[bool, pydantic.Field(alias='Azimuth overcurrent motor 2')]
    ElevationMode: pydantic.typing.Annotated[ElevationModeEnum, pydantic.Field(alias='Elevation mode')]
    ElevationCommandedPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation commanded position')]
    ElevationCurrentPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation current position')]
    ElevationCurrentVelocity: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation current velocity')]
    ElevationAveragePositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation average position error')]
    ElevationPeakPositionError: pydantic.typing.Annotated[float, pydantic.Field(alias='Elevation peak position error')]
    ElevationComputerDisabled: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation computer disabled')]
    ElevationAxisDisabled: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation axis disabled')]
    ElevationAxisInStop: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation axis in stop')]
    ElevationBrakesReleased: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation brakes released')]
    ElevationStopAtLCP: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation stop at LCP')]
    ElevationPowerOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation power on')]
    ElevationDownLimitEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Down limit: emergency')]
    ElevationDownLimitOperating: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Down limit: operating')]
    ElevationDownLimitPreLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Down limit: pre-limit')]
    ElevationDownLimitOperatingAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Down limit: operating (ACU software limit)')]
    ElevationDownLimitPreLimitAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Down limit: pre-limit (ACU software limit)')]
    ElevationUpLimitPreLimitAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Up limit: pre-limit (ACU software limit)')]
    ElevationUpLimitOperatingAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Up limit: operating (ACU software limit)')]
    ElevationUpLimitPreLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Up limit: pre-limit')]
    ElevationUpLimitOperating: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Up limit: operating')]
    ElevationUpLimitEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation Up limit: emergency')]
    ElevationSummaryFault: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation summary fault')]
    ElevationServoFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation servo failure')]
    ElevationMotionError: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation motion error')]
    ElevationBrake1Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation brake 1 failure')]
    ElevationBreakerFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation breaker failure')]
    ElevationAmplifier1Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation amplifier 1 failure')]
    ElevationMotor1Overtemp: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation motor 1 overtemp')]
    ElevationOverspeed: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation overspeed')]
    ElevationAmplifierPowerCylceInterlock: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation amplifier power cylce interlock')]
    ElevationRegenerationResistor1Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation regeneration resistor 1 overtemperature')]
    ElevationCANBusAmplifier1CommunicationFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation CAN bus amplifier 1 communication failure')]
    ElevationEncoderFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation encoder failure')]
    ElevationOscillationWarning: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation oscillation warning')]
    ElevationOscillationAlarm: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation oscillation alarm')]
    ElevationImmobile: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation immobile')]
    ElevationOvercurrentMotor1: pydantic.typing.Annotated[bool, pydantic.Field(alias='Elevation overcurrent motor 1')]
    BoresightMode: pydantic.typing.Annotated[BoresightModeEnum, pydantic.Field(alias='Boresight mode')]
    BoresightCommandedPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Boresight commanded position')]
    BoresightCurrentPosition: pydantic.typing.Annotated[float, pydantic.Field(alias='Boresight current position')]
    BoresightComputerDisabled: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight computer disabled')]
    BoresightAxisDisabled: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight axis disabled')]
    BoresightAxisInStop: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight axis in stop')]
    BoresightBrakesReleased: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight brakes released')]
    BoresightStopAtLCP: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight stop at LCP')]
    BoresightPowerOn: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight power on')]
    BoresightCCWLimitEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CCW limit: emergency')]
    BoresightCCWLimitOperating: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CCW limit: operating')]
    BoresightCCWLimitPreLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CCW limit: pre-limit')]
    BoresightCCWLimitOperatingAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CCW limit: operating (ACU software limit)')]
    BoresightCCWLimitPreLimitAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CCW limit: pre-limit (ACU software limit)')]
    BoresightCWLimitPreLimitAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CW limit: pre-limit (ACU software limit)')]
    BoresightCWLimitOperatingAcuSoftwareLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CW limit: operating (ACU software limit)')]
    BoresightCWLimitPreLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CW limit: pre-limit')]
    BoresightCWLimitOperating: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CW limit: operating')]
    BoresightCWLimitEmergency: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CW limit: emergency')]
    BoresightSummaryFault: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight summary fault')]
    BoresightServoFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight servo failure')]
    BoresightMotionError: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight motion error')]
    BoresightBrake1Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight brake 1 failure')]
    BoresightBrake2Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight brake 2 failure')]
    BoresightBreakerFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight breaker failure')]
    BoresightAmplifier1Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight amplifier 1 failure')]
    BoresightAmplifier2Failure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight amplifier 2 failure')]
    BoresightMotor1Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight motor 1 overtemperature')]
    BoresightMotor2Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight motor 2 overtemperature')]
    BoresightAUX1ModeSelected: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight AUX 1 mode selected')]
    BoresightAUX2ModeSelected: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight AUX 2 mode selected')]
    BoresightOverspeed: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight overspeed')]
    BoresightAmplifierPowerCylceInterlock: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight amplifier power cylce interlock')]
    BoresightRegenerationResistor1Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight regeneration resistor 1 overtemperature')]
    BoresightRegenerationResistor2Overtemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight regeneration resistor 2 overtemperature')]
    BoresightCANBusAmplifier1CommunicationFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CAN bus amplifier 1 communication failure')]
    BoresightCANBusAmplifier2CommunicationFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight CAN bus amplifier 2 communication failure')]
    BoresightEncoderFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight encoder failure')]
    BoresightOscillationWarning: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight oscillation warning')]
    BoresightOscillationAlarm: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight oscillation alarm')]
    BoresightTachoFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight tacho failure')]
    BoresightImmobile: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight immobile')]
    BoresightOvercurrentMotor1: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight overcurrent motor 1')]
    BoresightOvercurrentMotor2: pydantic.typing.Annotated[bool, pydantic.Field(alias='Boresight overcurrent motor 2')]
    GeneralSummaryFault: pydantic.typing.Annotated[bool, pydantic.Field(alias='General summary fault')]
    EStopServoDriveCabinet: pydantic.typing.Annotated[bool, pydantic.Field(alias='E-Stop servo drive cabinet')]
    EStopServicePole: pydantic.typing.Annotated[bool, pydantic.Field(alias='E-Stop service pole')]
    EStopAzMovable: pydantic.typing.Annotated[bool, pydantic.Field(alias='E-Stop Az movable')]
    KeySwitchBypassEmergencyLimit: pydantic.typing.Annotated[bool, pydantic.Field(alias='Key Switch Bypass Emergency Limit')]
    PCUOperation: pydantic.typing.Annotated[bool, pydantic.Field(alias='PCU operation')]
    Safe: bool
    PowerFailureLatched: pydantic.typing.Annotated[bool, pydantic.Field(alias='Power failure (latched)')]
    LightningProtectionSurgeArresters: pydantic.typing.Annotated[bool, pydantic.Field(alias='Lightning protection surge arresters')]
    PowerFailureNotLatched: pydantic.typing.Annotated[bool, pydantic.Field(alias='Power failure (not latched)')]
    PowerFailure24V: pydantic.typing.Annotated[bool, pydantic.Field(alias='24V power failure')]
    GeneralBreakerFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='General Breaker failure')]
    CabinetOvertemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Cabinet Overtemperature')]
    AmbientTemperatureLowOperationInhibited: pydantic.typing.Annotated[bool, pydantic.Field(alias='Ambient temperature low (operation inhibited)')]
    CoMovingShieldOff: pydantic.typing.Annotated[bool, pydantic.Field(alias='Co-Moving Shield off')]
    PLCACUInterfaceError: pydantic.typing.Annotated[bool, pydantic.Field(alias='PLC-ACU interface error')]
    QtyOfFreeProgramTrackStackPositions: pydantic.typing.Annotated[int, pydantic.Field(alias='Qty of free program track stack positions')]
    ACUInRemoteMode: pydantic.typing.Annotated[bool, pydantic.Field(alias='ACU in remote mode')]
    ACUFanFailure: pydantic.typing.Annotated[bool, pydantic.Field(alias='ACU fan failure')]
    CabinetUndertemperature: pydantic.typing.Annotated[bool, pydantic.Field(alias='Cabinet undertemperature')]
    TimeSynchronisationError: pydantic.typing.Annotated[bool, pydantic.Field(alias='Time synchronisation error')]
    ACUPLCCommunicationError: pydantic.typing.Annotated[bool, pydantic.Field(alias='ACU-PLC communication error')]
    StartOfProgramTrackTooEarly: pydantic.typing.Annotated[bool, pydantic.Field(alias='Start of Program Track too early')]
    TurnaroundAccelerationTooHigh: pydantic.typing.Annotated[bool, pydantic.Field(alias='Turnaround acceleration too high')]
    TurnaroundTimeTooShort: pydantic.typing.Annotated[bool, pydantic.Field(alias='Turnaround time too short')]
    class Config:
        populate_by_name = True

