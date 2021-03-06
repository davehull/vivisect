cmn_tests = (\
	{ "setup" : ( ("r0",32767),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32767),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32768),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",32769),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x0), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217727),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217728),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",134217729),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",32767),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",32768),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",32769),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",134217727),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",134217728),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",134217729),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x90000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483647),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x60000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x80000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x70000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483648),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x30000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",2147483647),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x60000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",2147483648),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x30000000), ("r4", 0x0) ), },
	{ "setup" : ( ("r0",2147483649),("r2",2147483649),("r4",0),("cpsr",0), ),    "tests" : ( ("cpsr", 0x30000000), ("r4", 0x0) ), },
)
