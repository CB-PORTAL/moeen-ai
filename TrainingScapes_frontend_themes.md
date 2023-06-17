# TrainingScapes_frontend_themes

- [GenesisLayer_v1](#GenesisLayer_v1_component_tree)
- [ThePlayground_v1](#ThePlayground_v1_component_tree)

## GenesisLayer_v1_component_tree

├── GenesisLayer_v1
│   ├── SmartExpandableWindowComponent
│   │   └── OverlayComponent
│   │       ├── TransparencyComponent
│   │       │   ├── TransparencyLevel [90%]
│   │       │   └── TransparencyShade ["#7CFB25"] \\ green.
│   │       └── ControlCenterComponent
│   │           ├── LearningModeComponent
│   │           │   ├── OnComponent
│   │           │   │   ├── Status [Bright Green]
│   │           │   │   └── LearningMode_BrainComponent
│   │           │   │       └── CollectsAndRecordsToDatasets_AILearnsComponent
│   │           │   └── OffComponent
│   │           │       └── Status [Turned Off]
│   │           ├── TrainingModeComponent
│   │           │   ├── OnComponent
│   │           │   │   ├── Status [Bright Green]
│   │           │   │   └── TrainingMode_BrainComponent
│   │           │   │       └── ProcessesDatasets_AITrainsComponent
│   │           │   └── OffComponent
│   │           │       └── Status [Turned Off]
│   │           ├── CommandCenterComponent 
│   │           │   ├── OnComponent
│   │           │   │   ├── Status [Bright Green]
│   │           │   │   └── MetaKnowCommandCenterComponent
│   │           │   └── OffComponent
│   │           │       └── Status [Turned Off]
│   │           ├── SessionsWindowComponent
│   │           │   ├── OnComponent
│   │           │   │   ├── Status [Bright Green]
│   │           │   │   └── SessionOverviewComponent
│   │           │   └── OffComponent
│   │           │       └── Status [Turned Off]
│   │           ├── AccountSettingsComponent
│   │           │   ├── OnComponent
│   │           │   │   ├── Status [Bright Green]
│   │           │   │   └── AccountSettingsAndCustomizationsMenuComponent
│   │           │   └── OffComponent
│   │           │       └── Status [Turned Off]
│   │           └── AskMoeenComponent
│   │               ├── OnComponent
│   │               │   ├── Status [Bright Green]
│   │               │   └── TalkToMoeenToProcessCommands_AIActionComponent
│   │               └── OffComponent
│   │                   └── Status [Turned Off]
│   └── SmartCursorComponent
│       ├── CursorPositionTrackingComponent
│       ├── UserInteractionInterpreterComponent
│       └── AIAdaptationRelayComponent

## ThePlayground_v1_component_tree

└── ThePlayground_v1
    ├── FunExpandableWindowComponent
    │   └── PlayfulOverlayComponent
    │       ├── ColorfulTransparencyComponent
    │       │   ├── TransparencyLevel [90%]
    │       │   └── TransparencyShade ["#FFD700"] // gold.
    │       └── GameControlCenterComponent
    │           ├── PlayModeComponent
    │           │   ├── ActiveComponent
    │           │   │   ├── Status [Bright Gold]
    │           │   │   └── PlayMode_JoyComponent
    │           │   │       └── CollectsAndRecordsToDatasets_AILearnsComponent
    │           │   └── InactiveComponent
    │           │       └── Status [Turned Off]
    │           ├── ExerciseModeComponent
    │           │   ├── ActiveComponent
    │           │   │   ├── Status [Bright Gold]
    │           │   │   └── ExerciseMode_PlayComponent
    │           │   │       └── ProcessesDatasets_AITrainsComponent
    │           │   └── InactiveComponent
    │           │       └── Status [Turned Off]
    │           ├── FunCommandCenterComponent 
    │           │   ├── ActiveComponent
    │           │   │   ├── Status [Bright Gold]
    │           │   │   └── MetaPlayCommandCenterComponent
    │           │   └── InactiveComponent
    │           │       └── Status [Turned Off]
    │           ├── PlaySessionsWindowComponent
    │           │   ├── ActiveComponent
    │           │   │   ├── Status [Bright Gold]
    │           │   │   └── SessionOverviewComponent
    │           │   └── InactiveComponent
    │           │       └── Status [Turned Off]
    │           ├── UserSettingsComponent
    │           │   ├── ActiveComponent
    │           │   │   ├── Status [Bright Gold]
    │           │   │   └── UserSettingsAndCustomizationsMenuComponent
    │           │   └── InactiveComponent
    │           │       └── Status [Turned Off]
    │           └── AskMoeenComponent
    │               ├── ActiveComponent
    │               │   ├── Status [Bright Gold]
    │               │   └── TalkToMoeenToProcessCommands_AIActionComponent
    │               └── InactiveComponent
    │                   └── Status [Turned Off]
    └── PlayfulCursorComponent
        ├── CursorPositionTrackingComponent
        ├── UserInteractionInterpreterComponent
        └── AIAdaptationRelayComponent