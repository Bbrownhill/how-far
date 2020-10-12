# How Far?
Welcome to How Far

If you often wonder how far away is Mars right now or about the current distance between Jupiter and Saturn?
Look no further!


How Far is a click application that gathers data from the JPL Horizons database and displays a realtime output of the distance between two planetary bodies.

## Installation

To install from Pypi:
Simply run:
`pip install how_far`

Or to install from source:
`pip install .`


## Usage

`how_far to <planet or moon> [-f/-from <other planet or moon>]`

If the -f/-from option is not specified the centre point defaults to Earth.

Please note: this CLI tool is case sensitive so remember to capitalise names.

i.e. Jupiter instead of jupiter.

Listed below are the possible selections.
List of Major bodies:
 * Sol
 * Mercury
 * Venus
 * Earth
 * Mars
 * Ceres
 * Jupiter
 * Saturn
 * Uranus
 * Neptune
 * Pluto

Table of Moons(Named moons only):

| Earth    | Mars   | Jupiter    | Saturn     | Uranus    | Neptune   | Pluto  |
|----------|--------|------------|------------|-----------|-----------|--------|
| The Moon | Phobos | Io         | Mimas      | Ariel     | Triton    | Charon |
|          | Deimos | Europa     | Enceladus  | Umbriel   | Nereid    |        |
|          |        | Ganymede   | Tethys     | Titania   | Naiad     |        |
|          |        | Callisto   | Dione      | Oberon    | Thalassa  |        |
|          |        | Amalthea   | Rhea       | Miranda   | Despina   |        |
|          |        | Himalia    | Titan      | Cordelia  | Galatea   |        |
|          |        | Elara      | Hyperion   | Ophelia   | Larissa   |        |
|          |        | Pasiphae   | Iapetus    | Bianca    | Proteus   |        |
|          |        | Sinope     | Phoebe     | Cressida  | Halimede  |        |
|          |        | Lysithea   | Janus      | Desdemona | Psamathe  |        |
|          |        | Carme      | Epimetheus | Juliet    | Sao       |        |
|          |        | Ananke     | Helene     | Portia    | Laomedeia |        |
|          |        | Leda       | Telesto    | Rosalind  | Neso      |        |
|          |        | Thebe      | Calypso    | Belinda   |           |        |
|          |        | Adrastea   | Atlas      | Puck      |           |        |
|          |        | Metis      | Prometheus | Caliban   |           |        |
|          |        | Callirrhoe | Pandora    | Sycorax   |           |        |
|          |        | Themisto   | Pan        | Prospero  |           |        |
|          |        | Megaclite  | Ymir       | Setebos   |           |        |
|          |        | Taygete    | Paaliaq    | Stephano  |           |        |
|          |        | Chaldene   | Tarvos     | Trinculo  |           |        |
|          |        | Harpalyke  | Ijiraq     | Francisco |           |        |
|          |        | Kalyke     | Suttungr   | Margaret  |           |        |
|          |        | Iocaste    | Kiviuq     | Ferdinand |           |        |
|          |        | Erinome    | Mundilfari | Perdita   |           |        |
|          |        | Isonoe     | Albiorix   | Mab       |           |        |
|          |        | Praxidike  | Skathi     | Cupid     |           |        |
|          |        | Autonoe    | Erriapus   |           |           |        |
|          |        | Thyone     | Siarnaq    |           |           |        |
|          |        | Hermippe   | Thrymr     |           |           |        |
|          |        | Aitne      | Narvi      |           |           |        |
|          |        | Eurydome   | Methone    |           |           |        |
|          |        | Euanthe    | Pallene    |           |           |        |
|          |        | Euporie    | Polydeuces |           |           |        |
|          |        | Orthosie   | Daphnis    |           |           |        |
|          |        | Sponde     | Aegir      |           |           |        |
|          |        | Kale       | Bebhionn   |           |           |        |
|          |        | Pasithee   | Bergelmir  |           |           |        |
|          |        | Hegemone   | Bestla     |           |           |        |
|          |        | Mneme      | Farbauti   |           |           |        |
|          |        | Aoede      | Fenrir     |           |           |        |
|          |        | Thelxinoe  | Fornjot    |           |           |        |
|          |        | Arche      | Hati       |           |           |        |
|          |        | Kallichore | Hyrrokkin  |           |           |        |
|          |        | Helike     | Kari       |           |           |        |
|          |        | Carpo      | Loge       |           |           |        |
|          |        | Eukelade   | Skoll      |           |           |        |
|          |        | Cyllene    | Surtur     |           |           |        |
|          |        | Kore       | Anthe      |           |           |        |
|          |        | Herse      | Jarnsaxa   |           |           |        |
|          |        | Dia        | Greip      |           |           |        |
|          |        |            | Tarqeq     |           |           |        |
|          |        |            | Aegaeon    |           |           |        |
