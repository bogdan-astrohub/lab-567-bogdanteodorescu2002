def do_undo(undo_list: list, redo_list: list):
    '''
    Merge un pas inapoi un functionalitatile executate.
    :param undo_list: lista undo
    :param redo_list: lista redo
    :return:
    '''

    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(top_undo)
        return top_undo
    return None


def do_redo(undo_list: list, redo_list: list):
    '''
    Revine la pasul initial in functionalitatile executate.
    :param undo_list: lista undo
    :param redo_list: lista redo
    :return:
    '''
    if undo_list:
        top_redo = redo_list.pop()
        undo_list.append(top_redo)
        return top_redo
    return None