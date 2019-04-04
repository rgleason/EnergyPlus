
// Google Test Headers
#include <gtest/gtest.h>

// EnergyPlus Headers
#include <EnergyPlus/Coils/CoilCoolingDX.hh>

#include "Coils/CoilCoolingDXFixture.hh"

using namespace EnergyPlus;

TEST_F( CoilCoolingDXTest, CoilCoolingDXInput )
{
    std::string idf_objects = this->getCoilObjectString("coolingCoil", false, 2);
    EXPECT_TRUE(process_idf( idf_objects, false ));
    CoilCoolingDX thisCoil("coolingCoil");
    EXPECT_EQ("COOLINGCOIL", thisCoil.name);
    EXPECT_EQ("PERFORMANCEOBJECTNAME", thisCoil.performance.name);
}
//
//TEST_F( EnergyPlusFixture, CoilCoolingDXInputFullHierarchySingleModeSingleSpeed )
//{
//
//    std::string const idf_objects = delimited_string( {
//      "Coil:Cooling:DX,                        ",
//      " CoilName,                              ",
//      " EvapInletNode,                         ",
//      " EvapOutletNode,                        ",
//      " AvailSchedule,                         ",
//      " ZoneNameForCondenser,                  ",
//      " CondenserInletNode,                    ",
//      " CondenserOutletNode,                   ",
//      " ThisPerformance,                       ",
//      " CondensateCollectionTankName,          ",
//      " EvaporativeCondenserSupplyTankName;    ",
//      "Coil:Cooling:DX:CurveFit:Performance,   ",
//      " ThisPerformance,                       ",
//      " 100,                                   ",
//      " 0,                                     ",
//      " 1,                                     ",
//      " 100,                                   ",
//      " SwitchingMethodName,                   ",
//      " OperatingModeScheduleName,             ",
//      " 100,                                   ",
//      " 400,                                   ",
//      " BasinHeaterOpSchedule,                 ",
//      " OperatingMode1Name;                    ",
//      "Coil:Cooling:DX:CurveFit:OperatingMode, ",
//      " OperatingMode1Name,                    ",
//      " 12000,                                 ",
//      " 100,                                   ",
//      " 200,                                   ",
//      " 2.5,                                   ",
//      " 0.5,                                   ",
//      " 100,                                   ",
//      " 300,                                   ",
//      " Yes,                                   ",
//      " Evaporative,                           ",
//      " 200,                                   ",
//      " DiscreteStagedContinuousOrNotBacon,    ",
//      " 5,                                     ",
//      " Speed1Name;                            ",
//      "Coil:Cooling:DX:CurveFit:Speed,         ",
//      " Speed1Name,                            ",
//      " 0.8,                                   ",
//      " 0.745,                                 ",
//      " 3.1415926,                             ",
//      " 0.9,                                   ",
//      " 0.9,                                   ",
//      " 0.5,                                   ",
//      " 300,                                   ",
//      " 6.9,                                   ",
//      " 0.8,                                   ",
//      " CapFT,                                 ",
//      " CapFF,                                 ",
//      " EIRFT,                                 ",
//      " EIRFF,                                 ",
//      " PLFCurveName,                          ",
//      " 0.6,                                   ",
//      " WasteHeatFunctionCurve,                ",
//      " SHRFT,                                 ",
//      " SHRFF;                                 "
//    } );
//
//    bool ok = !process_idf( idf_objects, false );
//    CoilCoolingDX thisCoil("CoilName");
//    int i = 1;
//
//}


