import py
import pytest

from primechecker import log_parser


@pytest.fixture()
def echoes_log_a():
    return py.path.local(__file__).dirpath("test_files", "echoes_log_a.txt")


def test_parse_log(echoes_log_a):
    print(echoes_log_a)
    log = log_parser.parse_log(str(echoes_log_a))
    assert log.version == "3.2"
    assert log.seed == "1145919247"
    assert log.excluded_pickups == "23"
    assert log.item_entries == [
        log_parser.ItemEntry("Temple Grounds", "Hive Chamber A", "Power Bomb"),
        log_parser.ItemEntry("Temple Grounds", "Hall of Honored Dead", "Light Suit"),
        log_parser.ItemEntry("Temple Grounds", "Hive Chamber B", "Energy Tank 9"),
        log_parser.ItemEntry("Temple Grounds", "War Ritual Grounds", "Missile Expansion 18"),
        log_parser.ItemEntry("Temple Grounds", "Windchamber Gateway", "Missile Expansion 45"),
        log_parser.ItemEntry("Temple Grounds", "Transport to Agon Wastes", "Missile Expansion 37"),
        log_parser.ItemEntry("Temple Grounds", "Temple Assembly Site", "Ing Hive Key 2"),
        log_parser.ItemEntry("Temple Grounds", "Grand Windchamber", "Missile Expansion 33"),
        log_parser.ItemEntry("Temple Grounds", "Dynamo Chamber", "Missile Expansion 25"),
        log_parser.ItemEntry("Temple Grounds", "Storage Cavern B", "Energy Tank 4"),
        log_parser.ItemEntry("Temple Grounds", "Plain of Dark Worship", "Missile Expansion 29"),
        log_parser.ItemEntry("Temple Grounds", "Defiled Shrine", "Energy Tank 8"),
        log_parser.ItemEntry("Temple Grounds", "Communication Area", "Missile Expansion 6"),
        log_parser.ItemEntry("Temple Grounds", "GFMC Compound", "Energy Tank 6"),
        log_parser.ItemEntry("Temple Grounds", "GFMC Compound", "Echo Visor"),
        log_parser.ItemEntry("Temple Grounds", "Accursed Lake", "Grapple Beam"),
        log_parser.ItemEntry("Temple Grounds", "Fortress Transport Access", "Seeker Launcher"),
        log_parser.ItemEntry("Temple Grounds", "Profane Path", "Missile Expansion 4"),
        log_parser.ItemEntry("Temple Grounds", "Phazon Grounds", "Energy Tank 1"),
        log_parser.ItemEntry("Temple Grounds", "Ing Reliquary", "Missile Expansion 19"),
        log_parser.ItemEntry("Great Temple", "Transport A Access", "Power Bomb Expansion 1"),
        log_parser.ItemEntry("Great Temple", "Temple Sanctuary", "Missile Expansion 39"),
        log_parser.ItemEntry("Great Temple", "Transport B Access", "Missile Expansion 38"),
        log_parser.ItemEntry("Great Temple", "Main Energy Controller", "Violet Translator"),
        log_parser.ItemEntry("Great Temple", "Main Energy Controller", "Super Missile"),
        log_parser.ItemEntry("Agon Wastes", "Mining Plaza", "Missile Expansion 11"),
        log_parser.ItemEntry("Agon Wastes", "Mining Station Access", "Dark Suit"),
        log_parser.ItemEntry("Agon Wastes", "Mining Station B", "Cobalt Translator"),
        log_parser.ItemEntry("Agon Wastes", "Transport Center", "Boost Ball"),
        log_parser.ItemEntry("Agon Wastes", "Mining Station A", "Space Jump Boots"),
        log_parser.ItemEntry("Agon Wastes", "Ing Cache 4", "Beam Ammo Expansion 2"),
        log_parser.ItemEntry("Agon Wastes", "Junction Site", "Sky Temple Key 9"),
        log_parser.ItemEntry("Agon Wastes", "Storage A", "Energy Tank 14"),
        log_parser.ItemEntry("Agon Wastes", "Mine Shaft", "Sky Temple Key 4"),
        log_parser.ItemEntry("Agon Wastes", "Crossroads", "Missile Expansion 8"),
        log_parser.ItemEntry("Agon Wastes", "Sand Cache", "Power Bomb Expansion 5"),
        log_parser.ItemEntry("Agon Wastes", "Portal Access A", "Missile Expansion 28"),
        log_parser.ItemEntry("Agon Wastes", "Judgment Pit", "Sky Temple Key 3"),
        log_parser.ItemEntry("Agon Wastes", "Agon Temple", "Missile Expansion 12"),
        log_parser.ItemEntry("Agon Wastes", "Trial Tunnel", "Power Bomb Expansion 4"),
        log_parser.ItemEntry("Agon Wastes", "Central Mining Station", "Energy Tank 12"),
        log_parser.ItemEntry("Agon Wastes", "Warrior's Walk", "Missile Expansion 43"),
        log_parser.ItemEntry("Agon Wastes", "Sandcanyon", "Missile Expansion 7"),
        log_parser.ItemEntry("Agon Wastes", "Dark Agon Temple", "Power Bomb Expansion 7"),
        log_parser.ItemEntry("Agon Wastes", "Battleground", "Sky Temple Key 1"),
        log_parser.ItemEntry("Agon Wastes", "Battleground", "Missile Expansion 1"),
        log_parser.ItemEntry("Agon Wastes", "Agon Energy Controller", "Missile Expansion 31"),
        log_parser.ItemEntry("Agon Wastes", "Ventilation Area A", "Dark Agon Key 2"),
        log_parser.ItemEntry("Agon Wastes", "Command Center", "Power Bomb Expansion 6"),
        log_parser.ItemEntry("Agon Wastes", "Main Reactor", "Missile Expansion 20"),
        log_parser.ItemEntry("Agon Wastes", "Doomed Entry", "Missile Expansion 34"),
        log_parser.ItemEntry("Agon Wastes", "Sand Processing", "Energy Tank 2"),
        log_parser.ItemEntry("Agon Wastes", "Storage D", "Missile Expansion 5"),
        log_parser.ItemEntry("Agon Wastes", "Dark Oasis", "Missile Expansion 9"),
        log_parser.ItemEntry("Agon Wastes", "Storage B", "Dark Torvus Key 2"),
        log_parser.ItemEntry("Agon Wastes", "Feeding Pit", "Missile Expansion 26"),
        log_parser.ItemEntry("Agon Wastes", "Bioenergy Production", "Amber Translator"),
        log_parser.ItemEntry("Agon Wastes", "Ing Cache 1", "Spider Ball"),
        log_parser.ItemEntry("Agon Wastes", "Storage C", "Missile Expansion 2"),
        log_parser.ItemEntry("Agon Wastes", "Ing Cache 2", "Missile Expansion 32"),
        log_parser.ItemEntry("Torvus Bog", "Torvus Lagoon", "Dark Torvus Key 1"),
        log_parser.ItemEntry("Torvus Bog", "Portal Chamber", "Beam Ammo Expansion 3"),
        log_parser.ItemEntry("Torvus Bog", "Path of Roots", "Power Bomb Expansion 2"),
        log_parser.ItemEntry("Torvus Bog", "Forgotten Bridge", "Energy Tank 10"),
        log_parser.ItemEntry("Torvus Bog", "Great Bridge", "Sky Temple Key 2"),
        log_parser.ItemEntry("Torvus Bog", "Cache A", "Beam Ammo Expansion 4"),
        log_parser.ItemEntry("Torvus Bog", "Plaza Access", "Missile Expansion 27"),
        log_parser.ItemEntry("Torvus Bog", "Abandoned Worksite", "Sunburst"),
        log_parser.ItemEntry("Torvus Bog", "Poisoned Bog", "Power Bomb Expansion 8"),
        log_parser.ItemEntry("Torvus Bog", "Venomous Pond", "Sky Temple Key 6"),
        log_parser.ItemEntry("Torvus Bog", "Temple Access", "Energy Transfer Module"),
        log_parser.ItemEntry("Torvus Bog", "Torvus Plaza", "Energy Tank 5"),
        log_parser.ItemEntry("Torvus Bog", "Putrid Alcove", "Missile Expansion 30"),
        log_parser.ItemEntry("Torvus Bog", "Torvus Grove", "Sky Temple Key 7"),
        log_parser.ItemEntry("Torvus Bog", "Torvus Temple", "Missile Expansion 36"),
        log_parser.ItemEntry("Torvus Bog", "Dark Torvus Arena", "Missile Expansion 48"),
        log_parser.ItemEntry("Torvus Bog", "Dark Torvus Arena", "Sky Temple Key 8"),
        log_parser.ItemEntry("Torvus Bog", "Underground Tunnel", "Screw Attack"),
        log_parser.ItemEntry("Torvus Bog", "Meditation Vista", "Annihilator Beam"),
        log_parser.ItemEntry("Torvus Bog", "Dark Torvus Temple", "Missile Expansion 47"),
        log_parser.ItemEntry("Torvus Bog", "Cache B", "Energy Tank 11"),
        log_parser.ItemEntry("Torvus Bog", "Hydrodynamo Station", "Missile Expansion 21"),
        log_parser.ItemEntry("Torvus Bog", "Torvus Energy Controller", "Morph Ball Bomb"),
        log_parser.ItemEntry("Torvus Bog", "Undertemple Access", "Dark Visor"),
        log_parser.ItemEntry("Torvus Bog", "Gathering Hall", "Missile Expansion 16"),
        log_parser.ItemEntry("Torvus Bog", "Training Chamber", "Sonic Boom"),
        log_parser.ItemEntry("Torvus Bog", "Sacrificial Chamber", "Missile Expansion 46"),
        log_parser.ItemEntry("Torvus Bog", "Undertemple", "Missile Expansion 49"),
        log_parser.ItemEntry("Torvus Bog", "Undertemple", "Missile Expansion 24"),
        log_parser.ItemEntry("Torvus Bog", "Transit Tunnel South", "Dark Beam"),
        log_parser.ItemEntry("Torvus Bog", "Transit Tunnel East", "Ing Hive Key 3"),
        log_parser.ItemEntry("Torvus Bog", "Dungeon", "Dark Agon Key 3"),
        log_parser.ItemEntry("Torvus Bog", "Hydrochamber Storage", "Energy Tank 7"),
        log_parser.ItemEntry("Torvus Bog", "Undertransit One", "Missile Expansion 44"),
        log_parser.ItemEntry("Sanctuary Fortress", "Sanctuary Entrance", "Gravity Boost"),
        log_parser.ItemEntry("Sanctuary Fortress", "Reactor Core", "Dark Torvus Key 3"),
        log_parser.ItemEntry("Sanctuary Fortress", "Transit Station", "Missile Expansion 14"),
        log_parser.ItemEntry("Sanctuary Fortress", "Sanctuary Map Station", "Missile Expansion 42"),
        log_parser.ItemEntry("Sanctuary Fortress", "Hall of Combat Mastery", "Darkburst"),
        log_parser.ItemEntry("Sanctuary Fortress", "Main Research", "Missile Expansion 41"),
        log_parser.ItemEntry("Sanctuary Fortress", "Culling Chamber", "Missile Expansion 23"),
        log_parser.ItemEntry("Sanctuary Fortress", "Central Area Transport West", "Missile Expansion 3"),
        log_parser.ItemEntry("Sanctuary Fortress", "Dynamo Works", "Missile Expansion 22"),
        log_parser.ItemEntry("Sanctuary Fortress", "Dynamo Works", "Power Bomb Expansion 3"),
        log_parser.ItemEntry("Sanctuary Fortress", "Hazing Cliff", "Missile Expansion 15"),
        log_parser.ItemEntry("Sanctuary Fortress", "Watch Station", "Missile Launcher"),
        log_parser.ItemEntry("Sanctuary Fortress", "Hive Dynamo Works", "Dark Agon Key 1"),
        log_parser.ItemEntry("Sanctuary Fortress", "Sentinel's Path", "Energy Tank 13"),
        log_parser.ItemEntry("Sanctuary Fortress", "Watch Station Access", "Missile Expansion 35"),
        log_parser.ItemEntry("Sanctuary Fortress", "Aerial Training Site", "Missile Expansion 10"),
        log_parser.ItemEntry("Sanctuary Fortress", "Aerial Training Site", "Missile Expansion 40"),
        log_parser.ItemEntry("Sanctuary Fortress", "Main Gyro Chamber", "Missile Expansion 13"),
        log_parser.ItemEntry("Sanctuary Fortress", "Vault", "Light Beam"),
        log_parser.ItemEntry("Sanctuary Fortress", "Temple Access", "Ing Hive Key 1"),
        log_parser.ItemEntry("Sanctuary Fortress", "Hive Gyro Chamber", "Emerald Translator"),
        log_parser.ItemEntry("Sanctuary Fortress", "Hive Temple", "Sky Temple Key 5"),
        log_parser.ItemEntry("Sanctuary Fortress", "Sanctuary Energy Controller", "Missile Expansion 17"),
        log_parser.ItemEntry("Sanctuary Fortress", "Hive Entrance", "Energy Tank 3"),
        log_parser.ItemEntry("Sanctuary Fortress", "Aerie", "Beam Ammo Expansion 1"),
    ]