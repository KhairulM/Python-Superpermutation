import itertools
import sys

def unite(currRes, candidate, record):
    el_len = len(currRes)

    newCandidate = list(candidate)
    newRes = currRes
    newRecord = record

    while (len(newCandidate) > 0) and (len(newRes) < newRecord):
        left_record = None
        right_record = None
        j = 1

        while el_len - j > 0:
            # Bagian Kiri
            for i in range(0, len(newCandidate)):
                currCd = newCandidate[i]

                # Ambil el_len-j terbelakang dari candidate
                subCd = currCd[j:]
                # Ambil el_len-j terdepan dari newRes
                subRes = newRes[:el_len-j]
                """
                print("subRes", subRes)
                print("subCd", subCd)
                """
                # Cek apakah sama, jika sama left_record dan left_remove kemudian break
                if subRes == subCd:
                    left_record = currCd[:j]
                    newRes = left_record + newRes
                    newCandidate.remove(currCd)
                    break

            # Kalau gak bisa di bagian kiri, coba bagian kanan
            if left_record == None:
                for i in range(0, len(newCandidate)):
                    currCd = newCandidate[i]

                    # Ambil el_len-j terdepan dari candidate
                    subCd = currCd[:el_len-j]
                    # Ambil el_len - j terbelakang dari currRes
                    subRes = newRes[len(currRes) - (el_len - j):]
                    """
                    print("subRes", subRes)
                    print("subCd", subCd)
                    """
                    # Cek apakah sama, jika sama update farthest_right dan right_record, jika tidak update j
                    if subCd == subRes:
                        right_record = currCd[el_len-j:]
                        newRes = newRes + right_record
                        newCandidate.remove(currCd)
                        break

            if (left_record == None) and (right_record == None):
                j += 1

            else:
                #print(newRes)
                break

    if len(newCandidate) == 0:
        return True, newRes, len(newRes)
    else:
        return False, currRes, record

def superPermute(perm_list):
    perm_len = len(perm_list)
    len_record = 9999
    el_record = None

    for i in range(0, perm_len):
        currEl = perm_list[i]

        candidate_list = list(perm_list)
        candidate_list.remove(currEl)

        success, result, newRecord = unite(currEl, candidate_list, len_record)

        if success:
            len_record = newRecord
            el_record = result
            
    return el_record


def main():
    if len(sys.argv) < 2:
        print("[ERROR] : number of arguments did not meet")
    else:
        nbObj = int(sys.argv[1])
        obj_list = []
        perm_list = []

        for i in range(0, nbObj):
            obj_list.append(i+1)
        
        perm_list = list(itertools.permutations(obj_list, nbObj))

        result = superPermute(perm_list)

        print(result)
        print("Length : " + str(len(result)))

main()