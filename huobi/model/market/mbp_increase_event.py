from huobi.model.market import Mbp


class MbpIncreaseEvent:
    """
    increasement of price depth.

    :member
        ch: Topic of subscribed.
        timestamp: The UNIX formatted timestamp generated by server in UTC.
        data: The price depth.

    """

    def __init__(self):
        self.ch = ""
        self.ts = 0
        self.data = Mbp()

    @staticmethod
    def json_parse(json_data):
        mbp_event = MbpIncreaseEvent()
        mbp_event.ts = json_data.get("ts")
        mbp_event.ch = json_data.get("ch")
        mbp = Mbp.json_parse(json_data.get("tick", {}))
        mbp_event.data = mbp
        return mbp_event



    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.ch, format_data + "Topic")
        PrintBasic.print_basic(self.ts, format_data + "Timestamp")

        self.data.print_object(format_data + "\t")