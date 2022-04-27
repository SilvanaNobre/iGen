--
-- File generated with SQLiteStudio v3.1.1 on seg abr 25 09:25:29 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: AnalysisArea
CREATE TABLE AnalysisArea (AAreaId INTEGER PRIMARY KEY NOT NULL, AAreaDescription VARCHAR (50) UNIQUE NOT NULL);
INSERT INTO AnalysisArea (AAreaId, AAreaDescription) VALUES (1, 'North');
INSERT INTO AnalysisArea (AAreaId, AAreaDescription) VALUES (2, 'South');

-- Table: InterventionType
CREATE TABLE InterventionType (IntTypeId VARCHAR (3) PRIMARY KEY NOT NULL, IntTypeDescription VARCHAR (50) NOT NULL, NodeColor VARCHAR (15) UNIQUE NOT NULL);
INSERT INTO InterventionType (IntTypeId, IntTypeDescription, NodeColor) VALUES ('CCS', 'Clear Cut and Stamp Sprout', 'blue');
INSERT INTO InterventionType (IntTypeId, IntTypeDescription, NodeColor) VALUES ('CCR', 'Clear Cut and Renewal', 'red');
INSERT INTO InterventionType (IntTypeId, IntTypeDescription, NodeColor) VALUES ('ni', 'No Intervention', 'yellow');
INSERT INTO InterventionType (IntTypeId, IntTypeDescription, NodeColor) VALUES ('BST', 'Establishment from bareland', 'brown');

-- Table: Nodes
CREATE TABLE Nodes (NodeId INTEGER PRIMARY KEY NOT NULL, PreviousNode INTEGER NOT NULL DEFAULT (0), LiNode INTEGER NOT NULL DEFAULT (0), Stand INTEGER REFERENCES Stand ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE NOT NULL, Stratum INT REFERENCES Strata (StratumId) ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE NOT NULL, Area DECIMAL (10, 4) NOT NULL DEFAULT (0), Period INT NOT NULL DEFAULT (0), Intervention VARCHAR (3) REFERENCES InterventionType (IntTypeId) ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE NOT NULL, Age INT NOT NULL DEFAULT (0), AfterInt INT NOT NULL DEFAULT (0), NodeType VARCHAR (15) REFERENCES NodeType (NodeTypeId) ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE NOT NULL, AfterRenewal INT NOT NULL DEFAULT (0), RotationCount INT NOT NULL DEFAULT (1), Yield DECIMAL (8, 2) NOT NULL DEFAULT (0));
INSERT INTO Nodes (NodeId, PreviousNode, LiNode, Stand, Stratum, Area, Period, Intervention, Age, AfterInt, NodeType, AfterRenewal, RotationCount, Yield) VALUES (1, 0, 0, 1, 1, 100, -2, 'CCR', 0, 0, 'Initial', 0, 1, 0);
INSERT INTO Nodes (NodeId, PreviousNode, LiNode, Stand, Stratum, Area, Period, Intervention, Age, AfterInt, NodeType, AfterRenewal, RotationCount, Yield) VALUES (2, 0, 0, 2, 1, 100, -4, 'CCR', 0, 0, 'Initial', 0, 1, 0);
INSERT INTO Nodes (NodeId, PreviousNode, LiNode, Stand, Stratum, Area, Period, Intervention, Age, AfterInt, NodeType, AfterRenewal, RotationCount, Yield) VALUES (3, 0, 0, 3, 2, 100, -2, 'CCR', 0, 0, 'Initial', 0, 1, 0);
INSERT INTO Nodes (NodeId, PreviousNode, LiNode, Stand, Stratum, Area, Period, Intervention, Age, AfterInt, NodeType, AfterRenewal, RotationCount, Yield) VALUES (4, 0, 0, 4, 1, 100, -1, 'CCS', 0, 0, 'Initial', 7, 2, 0);
INSERT INTO Nodes (NodeId, PreviousNode, LiNode, Stand, Stratum, Area, Period, Intervention, Age, AfterInt, NodeType, AfterRenewal, RotationCount, Yield) VALUES (5, 0, 0, 5, 2, 100, -3, 'CCS', 0, 0, 'Initial', 6, 2, 0);
INSERT INTO Nodes (NodeId, PreviousNode, LiNode, Stand, Stratum, Area, Period, Intervention, Age, AfterInt, NodeType, AfterRenewal, RotationCount, Yield) VALUES (6, 0, 0, 6, 2, 100, -8, 'CCS', 0, 0, 'Initial', 7, 2, 0);
INSERT INTO Nodes (NodeId, PreviousNode, LiNode, Stand, Stratum, Area, Period, Intervention, Age, AfterInt, NodeType, AfterRenewal, RotationCount, Yield) VALUES (7, 0, 0, 7, 1, 100, 0, 'BST', 0, 0, 'Initial', 0, 1, 0);

-- Table: NodeType
CREATE TABLE NodeType (NodeTypeId VARCHAR (15) PRIMARY KEY, NodeTypeDescription VARCHAR (50));
INSERT INTO NodeType (NodeTypeId, NodeTypeDescription) VALUES ('Initial', 'Initial Node');
INSERT INTO NodeType (NodeTypeId, NodeTypeDescription) VALUES ('Middle', 'between Initial and Final Node');
INSERT INTO NodeType (NodeTypeId, NodeTypeDescription) VALUES ('Final', 'When we can no longer open it');
INSERT INTO NodeType (NodeTypeId, NodeTypeDescription) VALUES ('NoIntNode', 'There is no intervention');
INSERT INTO NodeType (NodeTypeId, NodeTypeDescription) VALUES ('Opened', 'Initial node already opened');

-- Table: Parameter
CREATE TABLE Parameter (ParameterId INTEGER PRIMARY KEY NOT NULL, ParameterDescription VARCHAR (50) NOT NULL, Variable VARCHAR (15) REFERENCES Variable (VariableId) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE NOT NULL, ParameterValue VARCHAR (50) NOT NULL, AArea INTEGER REFERENCES AnalysisArea (AAreaId) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE NOT NULL, UNIQUE (Variable, AArea));
INSERT INTO Parameter (ParameterId, ParameterDescription, Variable, ParameterValue, AArea) VALUES (1, 'Horizon', 'Horizon', '21', 1);
INSERT INTO Parameter (ParameterId, ParameterDescription, Variable, ParameterValue, AArea) VALUES (2, 'RegularNodeSize', 'RegularNodeSize', '200', 1);
INSERT INTO Parameter (ParameterId, ParameterDescription, Variable, ParameterValue, AArea) VALUES (3, 'NoIntNodeSize', 'NoIntNodeSize', '50', 1);
INSERT INTO Parameter (ParameterId, ParameterDescription, Variable, ParameterValue, AArea) VALUES (4, 'ModelTitle', 'ModelTitle', 'Regular Pulpmill Model', 1);
INSERT INTO Parameter (ParameterId, ParameterDescription, Variable, ParameterValue, AArea) VALUES (5, 'Years per period', 'YearsPerPeriod', '1', 1);

-- Table: Productivity
CREATE TABLE Productivity (Stratum INT, Age INT, Volume DECIMAL (8, 2), PRIMARY KEY (Stratum, Age), FOREIGN KEY (Stratum) REFERENCES Strata (StratumId));
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 0, 0);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 1, 60);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 2, 100);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 3, 140);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 4, 190);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 5, 210);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 6, 230);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 7, 250);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 8, 270);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 9, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 10, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 11, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 12, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 13, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 14, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 15, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 16, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 17, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 18, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 19, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 20, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 21, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 22, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 23, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 24, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 25, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 26, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 27, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 28, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 29, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (1, 30, 290);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 0, 0);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 1, 40);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 2, 80);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 3, 120);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 4, 140);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 5, 160);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 6, 180);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 7, 220);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 8, 260);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 9, 300);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 10, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 11, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 12, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 13, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 14, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 15, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 16, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 17, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 18, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 19, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 20, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 21, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 22, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 23, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 24, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 25, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 26, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 27, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 28, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 29, 305);
INSERT INTO Productivity (Stratum, Age, Volume) VALUES (2, 30, 305);

-- Table: Rule
CREATE TABLE Rule (RuleId INT PRIMARY KEY NOT NULL, LastIntervention VARCHAR (3) REFERENCES InterventionType (IntTypeId) ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE NOT NULL, NextIntervention VARCHAR (3) REFERENCES InterventionType (IntTypeId) ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE, RuleDescription VARCHAR (100));
INSERT INTO Rule (RuleId, LastIntervention, NextIntervention, RuleDescription) VALUES (1, 'CCR', 'CCR', 'After a clearcut followed by a renewal we can clear cut and renew');
INSERT INTO Rule (RuleId, LastIntervention, NextIntervention, RuleDescription) VALUES (2, 'CCS', 'CCR', 'After a clearcut followed by a sprout we can clear cut and renew');
INSERT INTO Rule (RuleId, LastIntervention, NextIntervention, RuleDescription) VALUES (3, 'CCR', 'CCS', 'After a clearcut followed by a sprout we can clear cut and renew');
INSERT INTO Rule (RuleId, LastIntervention, NextIntervention, RuleDescription) VALUES (4, 'BST', 'CCR', 'After a clearcut followed by a sprout we can clear cut and renew');
INSERT INTO Rule (RuleId, LastIntervention, NextIntervention, RuleDescription) VALUES (5, 'BST', 'CCS', 'After a clearcut followed by a sprout we can clear cut and renew');

-- Table: RuleCondition
CREATE TABLE RuleCondition (RuleId INT REFERENCES Rule (RuleId) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE NOT NULL, IfOrThen VARCHAR (4) NOT NULL, RuleVar VARCHAR (15) REFERENCES Variable (VariableId) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE NOT NULL, RuleExpression VARCHAR (100) NOT NULL, PRIMARY KEY (RuleId ASC, IfOrThen ASC, RuleVar ASC));
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'If', 'Age', '(6<=:Age<=7)or(1<=:Period<=3 and :Age>=8)');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'If', 'Yield', ':Yield>=155');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'Stand', '=:Stand');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'Stratum', '=:Stratum');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'Area', '=:Area');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'Age', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'AfterInt', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'AfterRenewal', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'RotationCount', '=1');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'Yield', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (4, 'Then', 'NodeType', '=''Middle''');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'If', 'Age', '(6<=:Age<=7)or(1<=:Period<=3 and :Age>=8)');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'If', 'Yield', ':Yield>=155');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'Stand', '=:Stand');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'Stratum', '=:Stratum');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'Area', '=:Area');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'Age', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'AfterInt', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'AfterRenewal', '=:AfterRenewal+1');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'RotationCount', '=2');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'Yield', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'Then', 'NodeType', '=''Middle''');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'If', 'Age', '(6<=:Age<=7)or(1<=:Period<=3 and :Age>=8)');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'If', 'Yield', ':Yield>=155');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'Stand', '=:Stand');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'Stratum', '=:Stratum');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'Area', '=:Area');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'Age', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'AfterInt', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'AfterRenewal', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'RotationCount', '=1');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'Yield', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (1, 'Then', 'NodeType', '=''Middle''');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'If', 'Age', '(6<=:Age<=7)or(1<=:Period<=3 and :Age>=8)');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'If', 'Yield', ':Yield>=155');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'Stand', '=:Stand');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'Stratum', '=:Stratum');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'Area', '=:Area');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'Age', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'AfterInt', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'AfterRenewal', '=:AfterRenewal+1');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'RotationCount', '=2');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'Yield', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'Then', 'NodeType', '=''Middle''');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'If', 'Age', '(6<=:Age<=7)or(1<=:Period<=3 and :Age>=8)');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'If', 'Yield', ':Yield>=155');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'Stand', '=:Stand');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'Stratum', '=:Stratum');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'Area', '=:Area');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'Age', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'AfterInt', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'AfterRenewal', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'RotationCount', '=1');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'Yield', '=0');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (2, 'Then', 'NodeType', '=''Middle''');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (5, 'If', 'RotationCount', ':RotationCount<=1');
INSERT INTO RuleCondition (RuleId, IfOrThen, RuleVar, RuleExpression) VALUES (3, 'If', 'RotationCount', ':RotationCount<=1');

-- Table: Stand
CREATE TABLE Stand (StandId INTEGER PRIMARY KEY, Stratum INT REFERENCES Strata (StratumId) ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE, AArea INTEGER REFERENCES AnalysisArea (AAreaId) ON DELETE NO ACTION ON UPDATE NO ACTION MATCH SIMPLE);
INSERT INTO Stand (StandId, Stratum, AArea) VALUES (1, 1, 1);
INSERT INTO Stand (StandId, Stratum, AArea) VALUES (2, 1, 1);
INSERT INTO Stand (StandId, Stratum, AArea) VALUES (3, 2, 1);
INSERT INTO Stand (StandId, Stratum, AArea) VALUES (4, 1, 1);
INSERT INTO Stand (StandId, Stratum, AArea) VALUES (5, 2, 1);
INSERT INTO Stand (StandId, Stratum, AArea) VALUES (6, 2, 1);
INSERT INTO Stand (StandId, Stratum, AArea) VALUES (7, 1, 1);

-- Table: Strata
CREATE TABLE Strata (StratumId INT PRIMARY KEY, StratumDescription VARCHAR (50));
INSERT INTO Strata (StratumId, StratumDescription) VALUES (1, 'Stratum 1');
INSERT INTO Strata (StratumId, StratumDescription) VALUES (2, 'Stratum 2');

-- Table: ValidRule
CREATE TABLE ValidRule (AArea INTEGER REFERENCES AnalysisArea (AAreaId) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE NOT NULL, Rule INTEGER REFERENCES Rule (RuleId) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE NOT NULL, PRIMARY KEY (AArea, Rule));
INSERT INTO ValidRule (AArea, Rule) VALUES (1, 1);
INSERT INTO ValidRule (AArea, Rule) VALUES (1, 2);
INSERT INTO ValidRule (AArea, Rule) VALUES (1, 3);
INSERT INTO ValidRule (AArea, Rule) VALUES (1, 4);
INSERT INTO ValidRule (AArea, Rule) VALUES (1, 5);

-- Table: Variable
CREATE TABLE Variable (VariableId VARCHAR (15) PRIMARY KEY NOT NULL, Scope VARCHAR (15) NOT NULL, Required BOOLEAN NOT NULL, VarType VARCHAR (10) NOT NULL, NoIntNodeUpdateRule VARCHAR (100));
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Stand', 'Node', 'False', 'Integer', '=:Stand');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Stratum', 'Node', 'False', 'Integer', '=:Stratum');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Area', 'Node', 'False', 'Decimal', '=:Area');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Period', 'Node', 'True', 'Integer', '=:Period+1');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Intervention', 'Node', 'True', 'String', '=''ni''');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Age', 'Node', 'False', 'Integer', '=:Age+1');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('AfterInt', 'Node', 'False', 'Integer', '=:AfterInt+1');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('NodeType', 'Node', 'True', 'String', '=''NoIntNode''');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('AfterRenewal', 'Node', 'False', 'Integer', '=:AfterRenewal+1');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('RotationCount', 'Node', 'False', 'Integer', '=:RotationCount');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Yield', 'Node', 'False', 'Decimal', '=SearchTable(Productivity,(:Stratum,:Age),Volume)');
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('YearsPerPeriod', 'General', 'True', 'Integer', NULL);
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('Horizon', 'General', 'True', 'Integer', NULL);
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('RegularNodeSize', 'General', 'True', 'Integer', NULL);
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('NoIntNodeSize', 'General', 'True', 'Integer', NULL);
INSERT INTO Variable (VariableId, Scope, Required, VarType, NoIntNodeUpdateRule) VALUES ('ModelTitle', 'General', 'True', 'Integer', NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
