class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # client が使っても良い
        pass # pass は文が必須な構文で何もしない場合に使用する

    def _unsafe_method(self):
        # client は使うべきではない
        pass


