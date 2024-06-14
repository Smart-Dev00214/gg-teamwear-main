import { getChoicesFromEnum } from "../../common/util/misc-util";

export enum PackingListStatusType {
  RECEIVED = 1,
  SHIPPED = 2,
}

export const PackingListStatusChoices = getChoicesFromEnum(
  PackingListStatusType
);
